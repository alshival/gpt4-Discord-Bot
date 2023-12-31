from app.config import *
from commands.bot_functions import *
from commands.on_message import gif_response

from commands.fefe import search_youtube
from commands.fefe import browser
from commands.fefe import finetune_fefe
from commands.datalle import Datalle

async def talk_to_fefe(ctx,message):
    fefe_model = await get_fefe_model()
    print(fefe_model)
    
    # Check if there is a .csv file attached. If so, run datalle
    if len(ctx.message.attachments)==1:
        url = ctx.message.attachments[0].url
        print(url)
        # get filename using regex
        file_info = re.search('([^\/]+$)',url)
        filename = file_info.group(0)
        filepath = 'app/downloads/' + filename
        filetype = re.search('\.(\w+)$',url).group(1)
        if filetype == 'csv':
            await Datalle.data_int(ctx,message)
            return
    # Pull URL content
    message = await browser.browse_urls(message)
    
    completion_limit = 1250
    db = await create_connection()
    messages = []

    enc = tiktoken.encoding_for_model(fefe_model)
    
    sample_prompts = await finetune_fefe.sample_prompts(ctx)
    
    sample_string = json.dumps(sample_prompts)
    sample_tokens = len(enc.encode(sample_string))
    messages.extend(sample_prompts)

    # Check tokens for latest prompt
    new_prompt = {"role": "user", "content": f"{ctx.author.mention}: {message}"}
    latest_string = json.dumps(new_prompt)
    latest_token = len(enc.encode(latest_string))
    
    # Load in past prompts
    past_prompts = await fetch_prompts(db,str(ctx.channel.id), 3)
    past_prompts = check_tokens(
        past_prompts,
        fefe_model,
        completion_limit + latest_token + sample_tokens
    ) 

    messages.extend(past_prompts)

    # Load newest prompt
    messages.append(new_prompt)
    
    # Generate a response using the 'gpt-3.5-turbo' model
    response = openai.ChatCompletion.create(
        model=fefe_model,
        messages=messages,
        max_tokens=completion_limit,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.4,
        presence_penalty=0.6,
    )

    # Extract the response text and send it back to the user
    response_text = response['choices'][0]['message']['content']
    final_response = response_text
    ############
    # GIF
    ############
    #Check to see if it is a gif.
    check_if_gif = re.search(gif_regex_string,final_response)
    if check_if_gif:
        final_response = await gif_response.gif_search(final_response)
    ##############
    # Memorable
    ##############
    # Check if interaction is memorable
    memorable = re.search("MEMORABLE=(True|False)",final_response)
    if memorable:
        memorable_value =  memorable.group(1)
        # print(f'memorable is {memorable_value}')
        if memorable_value == 'True':
            await store_memory(db,json.dumps(new_prompt))
            await store_memory(db,json.dumps({'role':'assistant','content':response_text}))
        final_response = re.sub("MEMORABLE=(True|False)",'',final_response)
    else:
        re.sub("MEMORABLE=(True|False)",'',final_response)
        
    #################
    # Check reminder
    #################
    reminder = re.search('REMINDER=(\{[^}]*\})',final_response)
    if reminder:
        dict = ast.literal_eval(reminder.group(1))
        if ('time' in dict.keys()) & ('note' in dict.keys()):
            time = eval(dict['time'])
            note = dict['note']
            await store_reminder(db,ctx.author.name,time,note,ctx.channel.id,ctx.channel.name)
            print('reminder stored in database')

    final_response = re.sub('REMINDER=(\{[^}]*\})','',final_response)
    #################
    # Search Youtube
    #################
    youtube = re.search(youtube_regex_string,final_response)
    if youtube:
        search_query = youtube.group(1)
        if len(search_query)>0:
            try:
                search_results = await search_youtube.search_youtube(search_query)
                final_response = re.sub(youtube.group(0),'\n\n'+ search_results,final_response)
            except Exception as e:
                print(e)
                final_response = re.sub(youtube.group(0),'\n\n Oh... wait... I had some trouble finding results. Sorry :(',final_response)
    final_response = re.sub(youtube_regex_string,'',final_response)
    #################
    # Generate Image
    #################
    imagegen = re.search(imagegen_regex_string,final_response)
    
    if imagegen:
        search_query = imagegen.group(1)
        if len(search_query)>0:
            try:
                image_url = await generate_image(search_query)
                final_response = re.sub(imagegen.group(0),f'\n\n[Generated by openAi]({image_url})',final_response)
            except Exception as e:
                print(e)
                final_response = re.sub(imagegen.group(0),'\n\n Oh... wait... I had some trouble finding results. Sorry :(')
        else:
            final_response = re.sub(imagegen_regex_string,'',final_response)

    final_response = await clean_response(final_response)
    await send_chunks(ctx, final_response)
        
    # store the prompt
    await store_prompt(db,json.dumps(new_prompt),ctx.channel.id,ctx.channel.name,'fefe')
    await store_prompt(db,json.dumps({'role':'assistant','content':response_text}),ctx.channel.id,ctx.channel.name,'fefe')
    await db.close()