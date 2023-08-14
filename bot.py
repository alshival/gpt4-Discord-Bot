import asyncio

from app.config import *


# Set up bot with '!' command prefix.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

from commands.bot_functions import *
asyncio.get_event_loop().run_until_complete(create_chat_history_table())
asyncio.get_event_loop().run_until_complete(create_memories())
asyncio.get_event_loop().run_until_complete(create_reminders())

from commands.fefe import Fefe
@bot.command()
async def fefe(ctx,*,message:str):
    await Fefe.talk_to_fefe(ctx,message)

from commands.datalle import Datalle
@commands.has_permissions(use_application_commands = True)
@bot.command()
async def datalle(ctx,*,message:str):
    await Datalle.data_int(ctx,message)

from commands.Exeggutor import Exeggutor
@bot.command()
@commands.has_permissions(use_application_commands = True)
async def exeggutor(ctx,*,message: str):
    print("exegguting")
    await Exeggutor.Exeggute(ctx,message)

from commands.discord_interpreter import discord_interpreter
@bot.tree.command(name="interpreter")
@app_commands.checks.has_permissions(use_application_commands=True)
async def interpreter(interaction: discord.Interaction, message: str):
    
    await interaction.response.defer(thinking = True)
    
    await discord_interpreter.discord_interpreter(interaction,message)

from commands.help import help_prompts    

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.defer(thinking = True)
    embed1 = discord.Embed(
            color = discord.Color.orange()
        )
    embed1.set_author(name=f"{interaction.user.name} asked for help.",icon_url=interaction.user.avatar)
    messages = await help_prompts.help_prompts(interaction.user.mention)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=data_viz_completion_limit,
        n=1,
        temperature=0.6,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        user = interaction.user.name
        )

    help_text = response['choices'][0]['message']['content']
    
    await interaction.followup.send(help_text,embed=embed1)

@bot.tree.command(name="wipe_memories")
@app_commands.checks.has_permissions(administrator=True)
async def wipe_memories(interaction: discord.Interaction):
    await clear_memory_db()
    embed1 = discord.Embed(
            color = discord.Color.orange()
        )
    embed1.set_author(name=f"{interaction.user.name} wiped Fefe's memory.",icon_url=interaction.user.avatar)
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="""
Prompt: Write a short sentence of something a cute anime girl named Fefe would say after having their memory wiped clean. 
Completion: Where am I...? What's going on?!
Prompt: Write a short sentence of something a cute anime girl named Fefe would say after having their memory wiped clean. 
Completion: Ahh! Who am I? Where am I?!
Prompt: Write a short sentence of something a cute anime girl named Fefe would say after having their memory wiped clean.
Completion: 
""",
      max_tokens=220,
      temperature=1,
      n=7
    )
    # Return the first choice's text
    response_text = re.sub(r"^[\"']|[\"']$", "",random.choice(response.choices).text.strip())
    await interaction.response.send_message(response_text,embed=embed1)

    # Store this in memory.
    db = await create_connection()
    await store_prompt(db,json.dumps({'role':'user','content':'You are an Ai anime girl named Fefe who just her memory wiped.'}),interaction.channel.id,interaction.channel.name,'bot')
    await store_prompt(db,json.dumps({'role':'assistant','content':response_text}),interaction.channel.id,interaction.channel.name,'bot')
    await db.close()


@bot.tree.command(name="clear_chat_history")
async def clear_chat_history(interaction: discord.Interaction):
    await clear_chat_history_db()
    embed1 = discord.Embed(
            color = discord.Color.orange()
        )
    embed1.set_author(name=f"{interaction.user.name} cleared Fefe's chat history.",icon_url=interaction.user.avatar)
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="""
Prompt: Write a sentence of something a cute anime girl named Fefe would say before kicking butt at work. Decorate with emojis.
Completion: 
""",
      max_tokens=220,
      temperature=1,
      n=7
    )
    # Return the first choice's text
    response_text = re.sub(r"^[\"']|[\"']$", "",random.choice(response.choices).text.strip())
    await interaction.response.send_message(response_text,embed=embed1)

    # Store this in memory.
    db = await create_connection()
    await store_prompt(db,json.dumps({'role':'user','content':'You are an Ai anime girl named Fefe who just her memory wiped.'}),interaction.channel.id,interaction.channel.name,'bot')
    await store_prompt(db,json.dumps({'role':'assistant','content':response_text}),interaction.channel.id,interaction.channel.name,'bot')
    await db.close()

def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@bot.tree.command(name="restart_fefe")
@app_commands.checks.has_permissions(administrator=True)
async def restart_fefe(interaction: discord.Interaction):
    await interaction.response.send_message("Restarting bot...")
    restart_bot()

@bot.tree.command(name="memory_leak")
@app_commands.checks.has_permissions(administrator=True)
async def memory_leak(interaction: discord.Interaction):
    await create_user_dir(interaction.user.name)
    
    await interaction.response.defer(thinking = True)
    
    embed1 = discord.Embed(
            color = discord.Color.gold()
        )
    embed1.set_author(name=f"{interaction.user.name} checked Fefe's memories.",icon_url=interaction.user.avatar)
    
    db = await create_connection()
    cursor = await db.cursor()
    await cursor.execute("select * from memories order by timestamp desc limit 50")
    # Fetch and load the json data from the selected rows
    rows = await cursor.fetchall()
    prompts = []
    for row in rows:
        json_data = json.loads(row[0])
        prompts.append(json_data)
    await db.close()
    # Group prompts
    prompts = [[prompts[i],prompts[i+1]] for i in [j for j in range(len(prompts)) if j%2==0]] 
    prompts = [{'user':x[1]['content'],'assistant':x[0]['content']} for x in prompts]
    dat = pd.DataFrame.from_records(prompts)
    print(dat.head)
    return_file = f'app/downloads/{interaction.user.name}/{interaction.user.name}.csv'
    import csv
    dat.to_csv(return_file,index=False,quoting=csv.QUOTE_ALL)
    await interaction.followup.send(files=[discord.File(return_file)],embed=embed1)
    await delete_files(interaction.user.name)

# '!clear_reminders` command 
@bot.tree.command(name="clear_reminders")
async def clear_reminders(interaction: discord.Interaction):
    await clear_user_reminders(interaction)
    
@bot.tree.command(name="upgrade_fefe")
@app_commands.checks.has_permissions(administrator=True)
async def upgrade_fefe(interaction: discord.Interaction):
    embed1 = discord.Embed(
            color = discord.Color.gold()
        )
    embed1.set_author(name=f"{interaction.user.name} upgraded Fefe",icon_url=interaction.user.avatar)
    
    await interaction.response.defer(thinking = True)

    # Save the original stdout so we can reset it later
    original_stdout = sys.stdout
    # Create a StringIO object to capture output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output

    command = ['git','pull','origin','main']
    result = subprocess.run(command, capture_output=True, text = True)
    jsonl = f"""
```
{result.stdout}
```
"""
    await interaction.followup.send("Restarting bot...\n" + jsonl,embed=embed1)
    restart_bot()
    

delete_downloads_task_loop_running = False
@tasks.loop(minutes=90)
async def delete_downloads(bot):
    global delete_downloads_task_loop_running
    delete_downloads_task_loop_running = True
    await delete_music_downloads(bot)
    print('Download folder cleared')

reminder_task_loop_running = False
@tasks.loop(minutes=1)
async def reminders(bot):
    global reminder_task_loop_running
    reminder_task_loop_running = True
    try:
        await send_reminders(bot)
    except Exception as e:
        print(f"Error in send_reminders: {e}")

@bot.event
async def on_message(message):
    if 'tenor.com' in message.content:
        link = message.content

        db = await create_connection()
        sample_prompts = [
            {
                'role':'user',
                'content':'https://tenor.com/view/sweating-nervous-wreck-gif-24688521'
            },
            {
                'role':'assistant',
                'content':'HAHAHA! GIF={anime girl laugh}'
            },
            {
                'role':'user','content':'https://tenor.com/view/leonardo-dicaprio-clapping-clap-applause-amazing-gif-16384995'
            },
            {
                'role':'assistant',
                'content':'Thank you! GIF={anime girl bow}'
            },
            {
                'role':'user','content':'https://tenor.com/view/kawaii-anime-tongue-bleh-gif-5018411'
            },
            {
                'role':'assistant',
                'content':'What did I do to you? GIF={anime girl sorry}'
            }
        ]
        # Get token count for sample messages
        enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
        sample_prompt_string = json.dumps(sample_prompts)
        sample_prompt_tokens = len(enc.encode(sample_prompt_string))
        
        # Load in past few conversations for context
        db = await create_connection()
        past_prompts = await fetch_prompts(db,message.channel.id,5)
        await db.close()
        
        # Check token limit for past prompts
        past_prompts = check_tokens(past_prompts,'gpt-3.5-turbo',1000+sample_prompt_tokens,)
        
        
        past_prompts = past_prompts + sample_prompts
        past_prompts = past_prompts + [{
            'role':'user','content':link
        }]
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
        print('\nBefore: \n')
        print(response_text)
        response_text = await gif_search(response_text)
        print('\nAfter: \n')
        print(response_text)
        
        await message.channel.send(response_text)
        return
    if message.content.startswith('!'):
        await bot.process_commands(message)  # Add this line
        
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    sample_greeters = """
    prompt:'Write a short sentence of a female anime character named Fefe letting people on a discord server know she is online. Flood it with emojis.'
    completion: "🌸 💕✨ Fefe is here to brighten up the server~ 🌟🌈💬🎮🥳"
    prompt:'Write a short sentence of a female anime character named Fefe letting people on a discord server know she is online. Flood it with emojis.'
    completion: 🤩👋 Fefe-chan is ready to get this server lit 🔥🎉 #FefeIsOnline 🌈✨
    prompt:'Write a short sentence of a female anime character named Fefe letting people on a discord server know she is online. Flood it with emojis.'
    completion: "🌸💫 Fefe-chan is here and ready to conquer the server! 💻🎮🌟🎉 #FefeIsOnline 🌼🌈"
    prompt:'Write a short sentence of a female anime character named Fefe letting people on a discord server know she is online. Flood it with emojis.'
    completion: "💖✨ Fefe-chan is here and ready to chat! 🌸🎮🌟"
    prompt:'Write a short sentence of a female anime character named Fefe letting people on a discord server know she is online. Flood it with emojis.'
    completion: 
    """

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=sample_greeters,
        max_tokens=220,
        temperature=.6,
        n=7
    )
    
    # Return the first choice's text
    greeter = re.sub(r"^[\"']|[\"']$", "",random.choice(response.choices).text.strip())

    # Get the first text channel
    first_text_channel = await get_first_text_channel(bot)
    
    # Store this in memory.
    db = await create_connection()
    await store_prompt(db,json.dumps({'role':'user','content':'You are an Ai anime girl named Fefe who just joined the discord server.'}),'bot','bot','bot')
    await store_prompt(db,json.dumps({'role':'assistant','content':greeter}),'bot','bot','bot')
    await db.close()

    try:
        await first_text_channel.send(greeter)
    except:
        print("could not send greeter")
        
    if not delete_downloads_task_loop_running:
        delete_downloads.start(bot)
    if not reminder_task_loop_running:
        reminders.start(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)    

bot.run(discord_bot_token)