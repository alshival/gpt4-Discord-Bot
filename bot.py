import asyncio

from app.config import *


# Set up bot with '!' command prefix.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

from commands.bot_functions import *
asyncio.get_event_loop().run_until_complete(create_chat_history_table())

from commands.fefe import Fefe
@bot.command()
async def fefe(ctx,*,message:str):
    await Fefe.talk_to_fefe(ctx,message)

from commands.datalle import Datalle
@commands.has_permissions(administrator = True)
@bot.command()
async def datalle(ctx,*,message:str):
    await Datalle.data_int(ctx,message)

from commands.Exeggutor import Exeggutor
@bot.command()
@commands.has_permissions(administrator = True)
async def exeggutor(ctx,*,message: str):
    print("exegguting")
    await Exeggutor.Exeggute(ctx,message)

from commands.discord_interpreter import discord_interpreter
@bot.tree.command(name="interpreter")
@app_commands.checks.has_permissions(administrator=True)
async def interpreter(interaction: discord.Interaction, message: str):
    
    await interaction.response.defer(thinking = True)
    
    await discord_interpreter.discord_interpreter(interaction,message)

help_text = """
👋 Hi, I'm Fefe! I live on this server. 🍓🦄✨

🤖 I am an AI-powered Discord bot with market research analysis capabilities created by [Alshival's Data Service](https://www.alshival.com/ai-discord-bots)! 💖⭐️

🎶 Ask me to play music for you over voice channels and set reminders! ⏰🎵


📝 Here's a quick rundown on how to use the app:

 1️⃣ Talk to Fefe
- `!fefe <message>`: Chat with me. Ask me to set reminders, play music over the voice channel, or ask me questions about code or certain topics.
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

def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@bot.tree.command(name="restart_fefe")
@app_commands.checks.has_permissions(administrator=True)
async def restart_fefe(interaction: discord.Interaction):
    await interaction.response.send_message("Restarting bot...")
    restart_bot()
    
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
    await interaction.followup.send(jsonl,embed=embed1)
    await interaction.followup.send("Restarting bot...")
    restart_bot()
    

delete_downloads_task_loop_running = False
@tasks.loop(minutes=90)
async def delete_downloads(bot):
    global delete_downloads_task_loop_running
    delete_downloads_task_loop_running = True
    await delete_music_downloads(bot)
    print('Download folder cleared')
    

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    if not delete_downloads_task_loop_running:
        delete_downloads.start(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)    
    first_text_channel = await get_first_text_channel(bot)
    
    await first_text_channel.send("I'm online! :heart:")
    
bot.run(discord_bot_token)