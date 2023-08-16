from app.config import *
from commands.bot_functions import *

async def gif_reply(ctx,message):
    if re.search('https://tenor.com',message.content) or re.search('.*media[0-9]*\.giphy.com/.*', message.content):
        sample_prompts = [
                {
                    'role':'user',
                    'content':'Return a response of the form `GIF={anime girl <expression>}`: https://tenor.com/view/kiss-gif-22640695'
                },
                {
                    'role':'assistant',
                    'content':'GIF={anime girl kiss}'
                },
                {
                    'role':'user',
                    'content':'Return a response of the form `GIF={anime girl <expression>}`: https://tenor.com/view/sweating-nervous-wreck-gif-24688521'
                },
                {
                    'role':'assistant',
                    'content':'GIF={anime girl laugh}'
                },
                {
                    'role':'user','content':'https://tenor.com/view/juno-michael-cera-paulie-bleeker-can-we-make-out-now-make-out-gif-4302667'
                },
                {
                    'role':'assistant',
                    'content':'GIF={Scott Pilgrim Ramona Flowers kiss}'
                },
                {
                    'role':'user','content':'https://tenor.com/view/leonardo-dicaprio-clapping-clap-applause-amazing-gif-16384995'
                },
                {
                    'role':'assistant',
                    'content':'GIF={anime girl bow}'
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

        choice = random.choice([0, 1])

        if choice == 0:
            final_response = await gif_search(final_response)
        else:
            final_response = await gif_translate(final_response)
        final_response = re.sub(gif_regex_string,'',final_response)
        await ctx.send(final_response)
        
async def sticker_reply(ctx,message):
    if len(message.stickers)>0:
        sample_prompts = [
                {
                    'role':'user',
                    'content':'Return a response of the form `STICKER={anime girl <expression>}`: [<StickerItem id=796140638093443092 name=\'Sad\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'STICKER={anime girl kiss}'
                },
                {
                    'role':'user',
                    'content':'Return a response of the form `STICKER={anime girl <expression>}`: [<StickerItem id=816086581509095424 name=\'Heya\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'STICKER={anime girl hello}'
                },
                {
                    'role':'user','content':'[<StickerItem id=749046077629399122 name=\'Hungry\' format=StickerFormatType.lottie>]'
                },
                {
                    'role':'assistant',
                    'content':'STICKER={anime girl eating}'
                },
                {
                    'role':'user','content':'[<StickerItem id=1022134923206856714 name=\'Link\' format=StickerFormatType.png>]'
                },
                {
                    'role':'assistant',
                    'content':'STICKER={zelda}'
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
        check_sticker = re.search(sticker_regex_string,final_response)
        if check_sticker:
            search_query = check_sticker.group(1)
            print('Sticker search query: '+ search_query)
            if len(search_query)>0:
                base_url = "http://api.giphy.com/v1/stickers/search"
                params = {
                    "api_key": giphy_api_token,
                    "q": search_query,
                    "limit": 5
                }
                response = requests.get(base_url,params=params)
                status_code = response.status_code
                if status_code == 200:
                    data = response.json()
                    translated_url = random.choice(data["data"])["images"]["downsized"]["url"]
                    print(translated_url)
                    final_response = re.sub(sticker_regex_string,f'\n[Powered by GIPHY]({translated_url})',final_response)
                else:
                    error_message = data.get("message","An error occured.")
                    return f"Error: {error_message}"
                final_response = re.sub(sticker_regex_string,'',final_response)
                await ctx.send(final_response)
                        
                    