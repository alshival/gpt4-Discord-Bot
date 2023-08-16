from app.config import *
from commands.bot_functions import *
# Get GIF
async def gif_search(response_text):
    check_gif = re.search(giphy_regex_string,response_text)
    if check_gif:
        search_query = check_gif.group(1)
        print('search: ' + search_query)
        print('GIF search query: '+search_query)
        if len(search_query)>0:

            giphy_api_call = f'https://api.giphy.com/v1/gifs/search?q={search_query}&api_key={giphy_api_token}&limit=3'
            
            if GIPHY_CONTENT_FILTER:
                giphy_api_call = giphy_api_call + '&rating=pg-13'
                
            gif_response = requests.get(giphy_api_call)
            data = gif_response.json()
            
            try:
                gif = random.choice(data['data'])
                gif_url = gif['images']['original']['url']
                response_text =  re.sub(giphy_regex_string,f'\n[Powered by GIPHY]({gif_url})',response_text)
            except Exception as E:
                response_text = re.sub(giphy_regex_string,'',response_text)
        else:
            response_text =  re.sub(giphy_regex_string,'',response_text)
                
    else:
        response_text = re.sub(giphy_regex_string,'',response_text)

    return response_text

# Translate GIF
async def gif_translate(response_text):
    check_gif = re.search(giphy_regex_string,response_text)
    if check_gif:
        search_query = check_gif.group(1)
        print('search: ' + search_query)
        print('GIF search query: '+search_query)
        if len(search_query)>0:
            
            base_url = "https://api.giphy.com/v1/gifs/translate"
            params = {
                "api_key": giphy_api_token,
                "s": search_query,
                'wierdness':6
            }
        
            response = requests.get(base_url, params=params)
            data = response.json()
            try:
                translated_url = data["data"]["images"]["downsized"]["url"]
                response_text =  re.sub(giphy_regex_string,f'\n[Powered by GIPHY]({translated_url})',response_text)
            except Exception as e:
                print("message", "An error occurred: {e}")
                response_text =  re.sub(giphy_regex_string,'',response_text)
        else:
            response_text =  re.sub(giphy_regex_string,'',response_text)
    else:
        response_text =  re.sub(giphy_regex_string,'',response_text)
    return response_text

# Sticker search
async def sticker_search(response_text):
    print('sticker_request: \n ' + response_text)
    check_sticker = re.search(giphy_regex_string,response_text)
    if check_sticker:
        search_query = check_sticker.group(1)
        print('search: ' + search_query)
        print('Sticker search query: '+ search_query)
        if len(search_query)>0:
            base_url = "http://api.giphy.com/v1/stickers/search"
            params = {
                "api_key": giphy_api_token,
                "q": search_query,
                "limit": 4
            }
            response = requests.get(base_url,params=params)
            status_code = response.status_code
            data = response.json()
            if len(data["data"])>0:
                translated_url = random.choice(data["data"])["images"]["downsized"]["url"]
                print(translated_url)
                response_text =  re.sub(giphy_regex_string,f'\n[Powered by GIPHY]({translated_url})',response_text)
            else:
                roll = random.choice([0,1])
                if roll == 0:
                    response_text = await gif_search(response_text)
                elif roll == 1:
                    response_text = await gif_translate(response_text)
    else:
        response_text = re.sub(giphy_regex_string,'test2',response_text)
    return response_text

async def giphy_response(response_text):
    roll = random.choice([0,1,2])
    if roll == 0:
        print('gif_search')
        return await gif_search(response_text)
    elif roll == 1:
        print('gif_translate')
        return await gif_translate(response_text)
    elif roll == 2:
        print('sticker_search')
        return await sticker_search(response_text)

async def gif_reply(ctx,message):
    if re.search('https://tenor.com',message.content) or re.search('.*media[0-9]*\.giphy.com/.*', message.content) or len(message.stickers)>0:
        sample_prompts = [
                {
                    'role':'user',
                    'content':'Return a response of the form `GIPHY={anime girl <expression>}`: https://tenor.com/view/kiss-gif-22640695'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl kiss}'
                },
                {
                    'role':'user',
                    'content':'Return a response of the form `GIPHY={anime girl <expression>}`: https://tenor.com/view/sweating-nervous-wreck-gif-24688521'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl laugh}'
                },
                {
                    'role':'user','content':'https://tenor.com/view/juno-michael-cera-paulie-bleeker-can-we-make-out-now-make-out-gif-4302667'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={Scott Pilgrim Ramona Flowers kiss}'
                },
                {
                    'role':'user','content':'https://tenor.com/view/leonardo-dicaprio-clapping-clap-applause-amazing-gif-16384995'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl bow}'
                }
            ]
        # Get token count for sample messages
        enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
        sample_prompt_string = json.dumps(sample_prompts)
        sample_prompt_tokens = len(enc.encode(sample_prompt_string))
        
        # Load in past few conversations for context
        db = await create_connection()
        past_prompts = await fetch_prompts(db,message.channel.id,3)
        await db.close()
        # Check token limit for past prompts
        past_prompts = check_tokens(past_prompts,'gpt-3.5-turbo',(1000+sample_prompt_tokens)/1.5,)
        link = message.content
        new_prompt = {
            'role':'user','content':link 
        }
        
        past_prompts = sample_prompts + past_prompts + [new_prompt]
        
        # Generate a response using the 'gpt-3.5-turbo' model
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=past_prompts,
            max_tokens=1000,
            n=1,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.5,
        )
        final_response = response['choices'][0]['message']['content']

        final_response = await giphy_response(final_response)
        await ctx.send(final_response)
        
async def sticker_reply(ctx,message):
    if len(message.stickers)>0:
        sample_prompts = [
                {
                    'role':'user',
                    'content':'Return a response of the form `GIPHY={anime girl <expression>}`: [<StickerItem id=796140638093443092 name=\'Sad\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl kiss}'
                },
                {
                    'role':'user',
                    'content':'Return a response of the form `GIPHY={anime girl <expression>}`: [<StickerItem id=816086581509095424 name=\'Heya\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl hello}'
                },
                {
                    'role':'user','content':'[<StickerItem id=749046077629399122 name=\'Hungry\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={anime girl eating}'
                },
                {
                    'role':'user','content':'[<StickerItem id=1022134923206856714 name=\'Link\' format=StickerFormatType.png>]'
                },
                {
                    'role':'assistant',
                    'content':'GIPHY={zelda}'
                }
            ]
        # Get token count for sample messages
        enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
        sample_prompt_string = json.dumps(sample_prompts)
        sample_prompt_tokens = len(enc.encode(sample_prompt_string))
        
        # Load in past few conversations for context
        db = await create_connection()
        past_prompts = await fetch_prompts(db,message.channel.id,3)
        await db.close()
        # Check token limit for past prompts
        past_prompts = check_tokens(past_prompts,'gpt-3.5-turbo',(1000+sample_prompt_tokens)/1.5,)
        new_prompt = {
            'role':'user','content':str(message.stickers)
        }
        
        past_prompts = sample_prompts + [new_prompt]
        
        # Generate a response using the 'gpt-3.5-turbo' model
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=past_prompts,
            max_tokens=1000,
            n=1,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.5,
        )
        final_response = response['choices'][0]['message']['content']
        print(final_response)
        
        final_response = await sticker_search(final_response)
        await ctx.send(final_response)
                        
                    