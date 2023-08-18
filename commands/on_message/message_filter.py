from commands.bot_functions import *
from commands.on_message import gif_response
from commands.fefe import browser

async def filter(bot,message):
    message_content = message.content
    # Ignore messages from the bot
    if message.author == bot.user:
        return
    # Get fefe message mode
    fefe_mode_value = await get_fefe_mode()
    ctx = await bot.get_context(message)
    # Download content for any non-Tenor urls:
    urls = await browser.browse_urls(message_content)

    # # Here, we ignore all comments with unsupported file types.
    # if message.attachments:
    #     print('message filter checking for messages')
    #     url = ctx.message.attachments[0].url
    #     print(url)
    #     file_info = re.search('([^\/]+$)',url)
    #     filename = file_info.group(0)
    #     filepath = 'app/downloads/' + filename
    #     filetype = re.search('\.(\w+)$',url).group(1)
    #     if filetype not in ['csv']:
    #         return

    # Check if datalle.
    if re.search('^!datalle.*',message_content.lower()):
        print('datalle')
        datalle_command = bot.get_command('datalle')
        await ctx.invoke(datalle_command,message=message.content)
        return
    # Check if Exeggutor
    if re.search('^!exeggutor.*',message_content.lower()):
        print('exeggutor')
        exeg_command = bot.get_command('exeggutor')
        await ctx.invoke(exeg_command,message=message_content)
        return
    if urls:
        print('downloading urls')
        for key, value in urls.items():
            message_content = re.sub(key,value,message_content)
        
        # Action for response_mode = 'when_called'
    if fefe_mode_value == 'when_called':
        # Respond if called
        if re.search('(^[!]?fefe.*)|(.*\sfefe.*)',message.content.lower()):
            ctx = await bot.get_context(message)
            fefe_command = bot.get_command('fefe')
            await ctx.invoke(fefe_command,message=message.content)
        else: # Otherwise, store in the database as 'listening'.
            await store_listening(bot,message)
            
    elif fefe_mode_value == 'every_message':
            # Run through Tenor response
        if re.search('https://tenor.com',message.content) or len(message.stickers)>0:
            await gif_response.gif_reply(ctx,message)
        else:
            fefe_command = bot.get_command('fefe')
            await ctx.invoke(fefe_command,message=message.content)