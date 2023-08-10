from app.config import *
from commands.bot_functions import *

async def talk_to_fefe(ctx,message):
    db = await create_connection()
    
    past_prompts = await fetch_prompts(db, ctx.channel.id, 10)
    # Need to check token limit. For `!fefe`, we are using 'gpt-3.5-turbo` until GPT4 scales and response time decreases.
    # We will pull at most 8 chats. Then, we will check the tokens to see if it falls beneath gpt-3.5-turbo's 4096 limit.
    messages = []

    for prompt, response in past_prompts:
        messages.extend([{'role': 'user', 'content': f"""Message:\n```\n{prompt}\n```\n"""}, {'role': 'assistant', 'content': response}])
    messages.append({'role': 'user', 'content': f"""Generate a text-based response or reply to casual conversations with `GIF: <search term>` to reply with a GIF. \n Message:\n```\n{message}\n```\n"""})
    
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
    # Check to see if it is a gif.
    check_if_gif = re.search('GIF:',response_text)
    if check_if_gif:
        search_query = re.sub('.*GIF:','',response_text)
        gif_response = requests.get(f'https://api.giphy.com/v1/gifs/search?q={search_query}&api_key={gify_api_token}&limit=4')
        data = gif_response.json()
        
        # Choose a random GIF from the results
        try:
            gif = random.choice(data['data'])
            response_text = gif['images']['original']['url']
        except Exception as e:
            response_text = "I was going to respond with a GIF, but I couldn't find the right one."
            print(e)
            
    if len(response_text) > 2000:
        await send_chunks(ctx, response_text)
    else:
        await ctx.send(response_text)
    # store the prompt
    await store_prompt(db, ctx.author.name, message, openai_model, response_text, ctx.channel.id,ctx.channel.name,source='fefe')
    await db.close()