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

help_text = """
👋 Hi, I'm Fefe! I live on this server. 🍓🦄✨

🤖 I am an AI-powered Discord bot with market research analysis capabilities created by [Alshival's Data Service](https://www.alshival.com/ai-discord-bots)! 💖⭐️

🎶 Ask me to play music for you over voice channels and set reminders! ⏰🎵


📝 Here's a quick rundown on how to use the app:

 1️⃣ Talk to Fefe
- `!fefe <message>`: Chat with me. Ask me to set reminders, generate images, or ask me questions about code or certain topics.
- `!datalle <message>`: Attach a `.csv` file and request charts be generated.
- `!exeggutor <python>`: Run raw python code.

2️⃣ There are also some slash commands that help:
- `/interpreter`: Use the Discord interpreter to execute Python code.
- `/upgrade_fefe`: Upgrade me.
- `/restart_fefe`: Restart me.

💼 If you're into finance, try using the Discord Interpreter at `/plugins Interpreter <message>` to generate stock market charts! 📈📉

You can ask me questions about code produced by `!datalle`, `!exeggutor`, and the Discord interpreter at `/plugins Interpreter` using `!fefe`. I will be happy to provide further assistance and explanations.

📚 You can grab the code and instructions needed to install me on your server by visiting our site. We can also customize the app and the AI for your server.

🚀 Join the fun and make the most of your Discord experience! If you have any questions or need help, feel free to reach out. 😄

Experience the power of data with Alshival's Data Service. 🍉🌟💕
"""

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    embed1 = discord.Embed(
            color = discord.Color.orange()
        )
    embed1.set_author(name=f"{interaction.user.name} asked for help.",icon_url=interaction.user.avatar)
    
    await interaction.response.send_message(help_text,embed=embed1)

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