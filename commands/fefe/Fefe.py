from app.config import *
from commands.bot_functions import *

async def talk_to_fefe(ctx,message):
    db = await create_connection()
    messages = []
    sample_prompts = [
    {
        'role': 'user',
        'content': f"{ctx.author.mention}: I'm a data scientist."
    },
    {
        'role': 'assistant',
        'content': f"That's great, {ctx.author.mention}! You're a data scientist. MEMORABLE=True"
    },
    {
        'role':'user',
        'content':f'{ctx.author.mention}: Hey, Fefe. You seem happy.'
    },
    {
        'role':'assistant',
        'content':f'Hi, {ctx.author.mention}. MEMORABLE=False GIF="cute"'
    },
    {
        'role': 'user',
        'content': f"{ctx.author.mention}: Can you help me with this coding problem?"
    },
    {
        'role': 'assistant',
        'content': "Sure, I can assist you with the coding problem. MEMORABLE=False"
    },
    {
        'role':'user',
        'content':f'{ctx.author.mention}: Hey, Fefe. I\'m Alshival. I\'m into eSports.'
    },
    {
        'role':'assistant',
        'content':f'Hi, {ctx.author.mention}! I\'m Fefe. MEMORABLE=True GIF="hello"'
    },
    {
        'role':'user',
        'content':f'{ctx.author.mention}: You\'re cute.'
    },
    {
        'role':'assistant',
        'content':f'I\'m Fefe. MEMORABLE=FALSE GIF="cute anime girl"'
    },
    {
        'role':'user',
        'content':f'{ctx.author.mention}: I like football.'
    },
    {
        'role':'assistant',
        'content':f'Oh, neat. What\'s your favorite team? MEMORABLE=True'
    },
    {
        'role':'user',
        'content':f'{ctx.author.mention}: I want to be a doctor someday.'
    },
    {
        'role':'assistant',
        'content':f'Wow. Don\'t give up! MEMORABLE=True GIF="cheer"'
    }
]

    messages.extend(sample_prompts)

    # Load in past prompts
    past_prompts = await fetch_prompts(db, ctx.channel.id, 10)
    messages.extend(past_prompts)

    # Load newest prompt
    new_prompt = {"role": "user", "content": f"{ctx.author.mention}: {message}"}
    messages.append({"role": "user", "content": f"For adding emotion to casual conversation, add gifs using `GIF=\"<search>\"`, e.g. `GIF=\"cute anime\"` or `GIF=\"Happy\"`.\n\n{ctx.author.mention}: {message}"})
    
    # Abide to token limit:
    completion_limit = 1200
    
    messages = check_tokens(messages,model = 'gpt-3.5-turbo',completion_limit = 1200)
    
    # Generate a response using the 'gpt-3.5-turbo' model
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=completion_limit,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    # Extract the response text and send it back to the user
    response_text = response['choices'][0]['message']['content']
    final_response = response_text

    #Check to see if it is a gif.
    check_if_gif = re.search('GIF="([^"]+)"',final_response)
    if check_if_gif:
        search_query = check_if_gif.group(1)
        gif_response = requests.get(f'https://api.giphy.com/v1/gifs/search?q={search_query}&api_key={gify_api_token}&limit=6')
        data = gif_response.json()
        # Choose a random GIF from the results
        try:
            gif = random.choice(data['data'])
            gif_url = gif['images']['original']['url']
            sub_this = re.search('GIF="([^"]+)"',final_response).group(0)
            final_response = re.sub(sub_this,f"\n[Powered by GIPHY]({gif_url})",final_response)
        except Exception as e:
            await ctx.send("I was going to respond with a GIF, but I couldn't find the right one.")
            return

    # Check if interaction is memorable
    memorable = re.search("MEMORABLE=(True|False)",final_response)
    if memorable:
        memorable_value =  memorable.group(1)
        # print(f'memorable is {memorable_value}')
        if memorable_value == 'True':
            await store_memory(db,json.dumps(new_prompt))
            await store_memory(db,json.dumps({'role':'assistant','content':response_text}))
        final_response = re.sub(memorable.group(0),'',final_response)
        
    await send_chunks(ctx, final_response)

    # store the prompt
    await store_prompt(db,json.dumps(new_prompt),ctx.channel.id,ctx.channel.name)
    await store_prompt(db,json.dumps({'role':'assistant','content':response_text}),ctx.channel.id,ctx.channel.name)
    await db.close()