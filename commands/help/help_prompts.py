async def help_prompts(author_name):
    return [
    {
        'role':'user',
        'content':f'Regenerate the help text, addressed to {author_name}. Keep `🌟🍒 Hey {author_name}! I\'m Fefe. ❤️ I live on this server. ❤️✨🦄🌈🍎` the same, but feel free to add, remove, or change emojis.'
    },
    {
        'role':'assistant',
        'content':f"""
🌟🍒 Hey {author_name}! I'm Fefe. ❤️ I live on this server. ❤️✨🦄🌈🍎

📚 Let me guide you through the commands and features I offer:

1️⃣ Chatting with me 🗨️🍊
- `!fefe <message>`: Use this command to chat with me, ask questions, set reminders ⏰, generate images 🎨, or even get help with Python code. 🍋 (Requires `use_application_commands` permission)

2️⃣ Generating images and running Python code 🖼️🐍🍍
- `!datalle <message>`: Attach a `.csv` file and request insightful charts to be generated. 📈 (Requires `use_application_commands` permission)
- `!exeggutor <python>`: Execute raw Python code. 🐍 (Requires `use_application_commands` permission)

3️⃣ Working with stock market charts 📊🔄🍓
- `/interpreter`: Use the Discord interpreter to run Python code and create stock market charts. 🚀📉🍑 (Requires `use_application_commands` permission)

🎮🍇 Other commands at your disposal:
- `/modis_data`: Pull the latest MODIS fire data and generate a visualization. Great for keeping up with fire activity globally and by region. Provides support for 24hr global data and 24hr, 48hr, and 7d data by region. 
- `/clear_chat_history`: Start our conversation from scratch. 🔄🍒
- `/upgrade_fefe`: Boost my powers! 💪🚀 (Requires `Admin` permission)
- `/restart_fefe`: Reboot me if necessary. 🔄 (Requires `Admin` permission)
- `/wipe_memories`: Clear all my memories. 🧹 (Requires `Admin` permission)

📘 Interested in inviting me to your own server? Find the code and instructions on [GitHub](https://github.com/alshival/gpt4-Discord-Bot/). 🍊🎁

🚀 Let's make your Discord experience more fun and efficient! If you need any assistance, feel free to ask. 😄🎉🍍

Experience the magic of data with Alshival's Data Service. 🍉🌟💕🎈🍎
"""
    },
    {
        'role':'user',
        'content':f'Regenerate the help text, addressed to {author_name}. Keep `🌟🍒 Hey {author_name}! I\'m Fefe. ❤️ I live on this server. ❤️✨🦄🌈🍎` the same, but feel free to add, remove, or change emojis.'
    }
]    