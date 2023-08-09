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