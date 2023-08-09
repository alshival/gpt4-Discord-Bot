from app.config import *
from commands.bot_functions import *

async def talk_to_fefe(ctx,message):
    db = await create_connection()
    
    past_prompts = await fetch_prompts(db, ctx.channel.id, 4)
    messages = []

    for prompt, response in past_prompts:
        messages.extend([{'role': 'user', 'content': prompt}, {'role': 'assistant', 'content': response}])
    messages.append({'role': 'user', 'content': message})

    # Generate a response using the 'gpt-3.5-turbo' model
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1200,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    # Extract the response text and send it back to the user
    response_text = response['choices'][0]['message']['content']
    if len(response_text) > 2000:
        await send_chunks(ctx, response_text)
    else:
        await ctx.send(response_text)
    # store the prompt
    await store_prompt(db, ctx.author.name, message, openai_model, response_text, ctx.channel.id,ctx.channel.name,source='fefe')
    await db.close()