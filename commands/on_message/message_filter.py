from commands.bot_functions import *
async def filter(bot,message):
    # Ignore messages from the bot
    if message.author == bot.user:
        return
    # Get fefe message mode
    fefe_mode_value = await get_fefe_mode()
    
    # Check if exegguting.
    if re.search('!exeggutor.*',message.content.lower()):
        ctx = await bot.get_context(message)
        exeg_command = bot.get_command('exeggutor')
        await ctx.invoke(exeg_command,message=message.content)
        
    # Action for response_mode = 'when_called'
    if fefe_mode_value == 'when_called':
        # Check if we are resonding to a GIF
        if re.search('https://tenor.com',message.content) or re.search('.*media[0-9]*\.giphy.com/.*', message.content):
            link = message.content
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
            response_text = response['choices'][0]['message']['content']
            if re.search(gif_regex_string,response_text):
                final_response = await gif_translate(response_text)
            else:
                final_response = response_text
            # Remove regex matches from Fefe's training data.
            final_response = await clean_response(final_response)
            print(final_response)
            await message.channel.send(final_response)
            await db.close()
            return
        # Respond if called
        elif re.search('(^[!]?fe.*)|(.*\sfe.*)',message.content.lower()):
            ctx = await bot.get_context(message)
            fefe_command = bot.get_command('fefe')
            await ctx.invoke(fefe_command,message=message.content)
        else: # Otherwise, store in the database as 'listening'.
            ctx = await bot.get_context(message)
            db = await create_connection()
            await store_prompt(db,
                               json.dumps(
                                   {
                                       'role':'user',
                                       'content':f"'{ctx.author.mention}': {message.content}"}),
                               message.channel.id,
                               message.channel.name,
                               'listening')
    elif fefe_mode_value == 'every_message':
            ctx = await bot.get_context(message)
            fefe_command = bot.get_command('fefe')
            await ctx.invoke(fefe_command,message=message.content)

# async def filter_old(message):
#     # Check the response mode. If set to 'when_called', we just store as listening.
#     fefe_mode_value = await get_fefe_mode()

            
#             await store_prompt(db,json.dumps({'role':'assistant','content':'I\'m listening and ready to respond when I am called.'}),message.channel.id,message.channel.name,'listening')
#             await clear_listening()
            
#     if message.attachments:
#         url = ctx.message.attachments[0].url
#         file_info = re.search('([^\/]+$)',url)
#         filename = file_info.group(0)
#         filepath = 'app/downloads/' + filename
#         filetype = re.search('\.(\w+)$',url).group(1)

#         if filetype != 'csv':
#             ctx = await bot.get_context(datalle)
#             datalle_command = bot.get_command('datalle')
#             await ctx.invoke(datalle_commands,message=message.content)
#     # Otherwise, check if it is a GIF to respond to it (only when fefe_mode_value = "every_message")
#     elif fefe_mode_value == "every_message":
        
#     elif re.search('https://tenor.com',message.content) or re.search('.*media[0-9]*\.giphy.com/.*', message.content):
#         link = message.content
#         db = await create_connection()
#         sample_prompts = [
#             {
#                 'role':'user',
#                 'content':'Return a response of the form `<response> GIF={anime girl <expression>}: https://tenor.com/view/kiss-gif-22640695'
#             },
#             {
#                 'role':'assistant',
#                 'content':'GIF={anime girl kiss}'
#             },
#             {
#                 'role':'user',
#                 'content':'Return a response of the form `<response> GIF={anime girl <expression>}: https://tenor.com/view/sweating-nervous-wreck-gif-24688521'
#             },
#             {
#                 'role':'assistant',
#                 'content':'GIF={anime girl laugh}'
#             },
#             {
#                 'role':'user','content':'https://tenor.com/view/juno-michael-cera-paulie-bleeker-can-we-make-out-now-make-out-gif-4302667'
#             },
#             {
#                 'role':'assistant',
#                 'content':'GIF={Scott Pilgrim Ramona Flowers kiss}'
#             },
#             {
#                 'role':'user','content':'https://tenor.com/view/leonardo-dicaprio-clapping-clap-applause-amazing-gif-16384995'
#             },
#             {
#                 'role':'assistant',
#                 'content':'GIF={anime girl bow}'
#             }
#         ]
#         # Get token count for sample messages
#         enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
#         sample_prompt_string = json.dumps(sample_prompts)
#         sample_prompt_tokens = len(enc.encode(sample_prompt_string))
        
#         # Load in past few conversations for context
#         db = await create_connection()
#         past_prompts = await fetch_prompts(db,message.channel.id,3)
#         await db.close()
#         # Check token limit for past prompts
#         past_prompts = check_tokens(past_prompts,'gpt-3.5-turbo',(1000+sample_prompt_tokens)/1.5,)
        
#         new_prompt = {
#             'role':'user','content':link 
#         }
        
#         past_prompts = sample_prompts + past_prompts + [new_prompt]

#         # Generate a response using the 'gpt-3.5-turbo' model
#         response = openai.ChatCompletion.create(
#             model='gpt-3.5-turbo',
#             messages=past_prompts,
#             max_tokens=1000,
#             n=1,
#             temperature=0.7,
#             top_p=1,
#             frequency_penalty=0.0,
#             presence_penalty=0.5,
#         )
#         response_text = response['choices'][0]['message']['content']
#         if re.search(gif_regex_string,response_text):
#             final_response = await gif_translate(response_text)
#         else:
#             final_response = response_text
#         # store in chat_history


#         # Remove regex matches from Fefe's training data.
#         final_response = await clean_response(final_response)
#         print(final_response)
#         await message.channel.send(final_response)
#         await db.close()
#         return

#     elif fefe_mode_value == 'every_message':
#         ctx = await bot.get_context(message)
#         fefe_command = bot.get_command('fefe')
#         await ctx.invoke(fefe_command,message=message.content)