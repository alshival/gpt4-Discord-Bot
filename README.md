# 🤖🔥 GPT-4 Discord Bot with Python Support 🐍🚀

Are you a parseltongue? Do you speak python? 🐍🔥📚📊⏰🎵🌟💻

🤩 Hi there, I'm Fefe, an Ai-powered scientific calculator 🧮 that also blows you GIF kisses 💋, powered by OpenAI's GPT-4 model. 

A coding girlfriend? Ummm... Yes, I guess you could call me that as well. I can help and keep you company during development projects. ❤️

I come with a host of features designed to make your Discord experience more interactive and fun! 🎉

🔔 I can set reminders for you, ensuring you never miss a deadline or forget about that important meeting. ⏰

💻 Need to write or execute some python code? No problem, I've got you covered, with help from DATALL-E, the Fefe Interpreter (formerly the Discord Interpreter), and Exeggutor.

🎨 I can even generate images based on your descriptions. 🖼️

📊 Have a .CSV file? Pass it to me and I'll pass it to DATALL-E so that you can visualize the data with beautifully designed charts and graphs. 📈

🧮 DATALL-E lets you generate charts or maps from .CSV data you upload as an attachment. Plus, I return the code used to generate the image, so you can vet the data on the charts.

🎥 Want to watch a YouTube video? Just ask, and I'll find it for you. 📺

🌐 I was created by [Alshival's Data Service](https://alshival.com) to enhance your Discord server experience. Whether you're using me for personal tasks, hanging out with friends, managing a study group, or overseeing a project, I'm here to help. Let's have some fun together! 🌟🚀💻🎉

REMARK: The bot uses GPT-4 for DATALL-E and Fefe Interpreter. In order to keep costs down though, Fefe herself uses GPT-3.5-turbo.
If you'd like to use pure GPT-4, it'll cost you daily about a cup of premium coffee (~ $5 to $7). Though a whole month of GPT-3.5-turbo usage costs much less. But Fefe's GIF responses are way better with GPT-4. I think pure GPT-4 is worth it. If you would like the pure GPT-4, change the value in `app/config.py`:
```
fefe_model = 'gpt-3.5-turbo'
# for GPT-4
fefe_model = 'gpt-4'
```

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
                <tr>
            <td colspan="2" style="width: 100%;">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/fractal%20(1).png?raw=True" alt="Data Interpreter">
            </td>
        </tr>
        <tr>
            <td style="width: 100%;" colspan="2">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-15%201.04.52%20AM.png?raw=True">
            </td>
        </tr>
        <tr>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-17%208.40.42%20PM.png?raw=True">
            </td>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-17%208.51.14%20PM.png?raw=True">
            </td>
        </tr>
        <tr>
            <td style="width: 100%" colspan="2">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-19%2012.20.50%20AM.png?raw=True">
            </td>
        </tr>
    </table>
</body>
</html>

Note: You can ask to save in `my user directory` instead of specifying a path. When a user calls Exeggutor, DATALL-E, or the fefe interpreter, a user directory is created. Any files that are placed in that directory are sent back to the user. You can ask Fefe Interpreter to `/interpreter export the iris dataset as a .pkl into my user directory`, for example. My username on the server is `alshival`, and my user directory is located at `app/downloads/alshival`. 

<div style="text-align: center;">
    <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-22%2011.25.52%20AM.png?raw=True">
</div>

Please note that this bot creates a back door to the hardware you are running the bot on, since it depends on the `exec` function. You can spit the output of `.bashrc`, revealing security keys, simply by creating a prompt. Essentially, the Ai can access all files in a sandbox. This is why Discord Interpreter is aimed for small study groups and small teams. It works very well in a virtual environment or on a dedicated raspberry pi. ⚠️🔒🔐

<img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-04%204.48.30%20PM%20(1).png?raw=True">

Study groups can benefit from a Discord bot that utilizes OpenAI's GPT models. Since AI can make mistakes, the python code used to generate the charts is returned within a python dictionary suitable for fine-tuning an OpenAI model for better performance. 📚🤖📈📉📊📝

Feel free to use this code as inspiration for utilizing othe models, or reach out to us at [support@alshival.com](mailto:support@alshival.com) 🌟📩🚀💻

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
        <tr>
            <td style="width: 100%;" colspan="2;">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-14%207.09.46%20PM.png?raw=True">
            </td>
        </tr>
    </table>
</body>
</html>

<img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-12%205.00.36%20AM.png?raw=True" alt="Image Description">
Note: Choropleth support currently under development and unstable. Once fine-tuning GPT-4 is available, this feature will be ironed-out.
<img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-09%204.32.11%20AM.png?raw=True" alt="Data Interpreter">

## Usage

- Use the command prefix `!` to interact with the bot:

  - `!fefe <message>`: Ask Fefe to write or debug code from `DATALL-E` and `Discord Interpreter`, or answer questions. She can also set reminders, generate images, and search youtube.
  - `!datalle`: (Admin) Attach a .CSV file and ask Fefe to generate charts or maps. Then ask `!fefe` to go over the code with you.
  - `!exeggutor`: (Admin) Exeggute raw python code. Ask `!fefe` to go over the code or any errors with you.
- The bot also includes the following slash commands:
  - `/interpreter <message>`: Use the Discord Interpreter to move files around on your PC or raspberry pi, or to generate financial charts. Then ask `!fefe` to go over the code with you.
  - `/fefe_mode`: Fefe can reply to every message or when called. If the mode is set to `when called`, she walks into a conversation with a bit of contextual information, e.g. the last 4 messages posted on the discord. If the mode is set to `every message`, Fefe will reply to GIFs and Stickers.
  - `/modis_data`: Download the latest MODIS data. Ask Fefe or Interpreter to make changes or discuss the code. If you do not see your region available, it is due to Discord's limit of 25 slash command choices. Comment out a region and uncomment your region in `commands/modis_data/modis_download.py`.
  - `/help`: Provides a quick rundown of how to use the app.
  - `/upgrade_fefe`: Pull the latest Github changes.
  - `/restart_fefe`: Restart the bot from within discord.

## Features

- Chat with the bot using OpenAI's GPT models
- Analyze your data in `.csv` format using `DATALL-E`.
- Perform Market Research Analysis using yfinance to create financial charts and mix charts with regression lines.

Admin can also utilize the `!exeggutor` function to run raw python code. Useful when testing code snippets generated by openAi.

# Installation
### Set up bot on Discord
- Set up your bot on the [Discord Developer Portal](https://discord.com/developers/applications) and invite it to your server.
- In the bot's settings, you can customize various options such as its username, profile picture, and permissions. Make sure to at least enable the "Presence Intent" and "Server Members Intent" if your bot requires them.
- Under the "Token" section, click on the "Copy" button to copy your bot token. This token is

### Set environmental variables
- Set the environmental variables referenced in `app/config.py`:
   - `DISCORD_BOT_TOKEN`
   - `OPENAI_API_KEY`
   - `google_api_key` for GIFS & searching youtube
       - ([YouTube Data API](https://developers.google.com/youtube/v3/getting-started))
       - [Install Google's gcloud client as well](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to)
       - [Tenor GIF API Setup](https://developers.google.com/tenor/guides/quickstart)
       -    
### Clone Repository
- Clone the repository:

   ```shell
   gh repo clone alshival/openAi-Discord-Bot
   ```

### Install the required dependencies:
We suggest installing the bot's python dependencies in a virtual environment. You will need ffmpeg on your system to play music via the voice channel: `sudo apt install ffmpeg`.
To install on a linux machine or linux subsystem:

  - Navigate to the directory where your `requirements.txt` file is located:
     ```shell
     cd /path/to/your/openAi-Discord-Bot/
     ```
     
  - Create and activate the virtual environment:
     ```
     python3 -m venv env
     source env/bin/activate
     ```

  - Run the following command to install the packages:
     ```shell
     pip3 install -r requirements.txt
     deactivate # deactivates the virtual environment
     ```
   
Wait for the installation to complete. Pip will read the `requirements.txt` file and automatically download and install the packages listed within it, along with their dependencies.

After successful installation, you should have all the required packages available for your Discord bot. You can then proceed with running your bot.

### Run the bot:
First activate the virtual environment:
 ```shell
 source env/bin/activate
 ```

 Then start the bot with the following:
  ```shell
  python3 bot.py
  ```

- Your bot should now be running and ready to connect to Discord.

### Inviting the bot to the server
To invite your bot to a server, go back to the Discord Developer Portal:
- Select your application and go to the "OAuth2" section in the left sidebar.
- In the "Scopes" section, select the "bot" checkbox.
- In the "Bot Permissions" section, choose the necessary permissions your bot requires. These permissions determine what actions your bot can perform in a server.
- Once you have selected the desired permissions, a URL will be generated under the "Scopes" section.
- Copy the generated URL and open it in a web browser.
- Select the server where you want to invite your bot and click "Authorize."
- Complete any additional steps or permissions requested by Discord.
- If everything goes well, your bot should be added to the selected server and ready to use.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please email [support@alshival.com](mailto:support@alshival.com?subject=openAI%20Discord%20Bot), open an issue, or submit a pull request.

# License

[Creative Commons Zero v1.0 Universal](LICENSE)
