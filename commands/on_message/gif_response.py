from app.config import *
from commands.bot_functions import *

# Get GIF
async def gif_search(response_text):
        # get the top 8 GIFs for the search term
    
    try:
        search_term = re.search(gif_regex_string,response_text).group(1)
    except:
        return response_text

    base_url = "https://tenor.googleapis.com/v2/search"
    
    params = {
        'q': search_term,
        'media_format': "gif,",
        'key': google_api_key,
        'client_key': 'fefe',
        'limit': 5
    }      
    r = requests.get(base_url, params=params)    
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        gif_url = random.choice(top_8gifs['results'])['media_formats']['gif']['url']
        return re.sub(gif_regex_string,f"\n[Powered by Tenor]({gif_url})",response_text)
    else:
        return response_text

async def gif_reply(ctx,message):
    if re.search('https://tenor.com',message.content) or len(message.stickers)>0:
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

        final_response = await gif_search(final_response)
        final_response = await clean_response(final_response)
        await ctx.send(final_response)
        
