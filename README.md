# 🤖🔥 GPT-4 Discord Bot with Python Support 🐍🚀

Are you a parseltongue? Do you speak python? 🐍🔥📚📊⏰🎵🌟💻

This Discord bot harnesses the power of OpenAI's GPT-4 model and provides additional functionalities like writing and executing code, generating data visualizations from `.CSV` files 📊📈, and more. It now also includes **Discord Interpreter**, which allows you to manage files on your computer or create financial charts using yfinance using natural language. This bot also includes a tool called, **DATALL-E**, which generates charts or maps using `.csv` data you upload as an attachment. The code used to generate the image is returned as well, so that the data on the charts can be vetted. 📈📉📊🔍

Created by [Alshival's Data Service](https://alshival.com) to enhance your Discord server experience. Whether it's for personal use, a group of friends, a study group, or project management, this bot has got you covered. 🌟🚀💻🎉

Please note that the Discord Interpreter creates a server vulnerability, since it depends on the `exec` function. You can spit the output of `.bashrc`, revealing security keys by creating a prompt. Essentially, the Ai can access all files in a sandbox. This is why Discord Interpreter is aimed for small study groups and small teams. It works very well in a virtual environment or on a dedicated raspberry pi. ⚠️🔒🔐

<img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-04%204.48.30%20PM%20(1).png?raw=True">

Study groups can benefit from a Discord bot that utilizes OpenAI's GPT models. Since AI can make mistakes, the python code used to generate the charts is returned within a python dictionary suitable for fine-tuning an OpenAI model for better performance. 📚🤖📈📉📊📝

Feel free to use this code as inspiration for utilizing othe models, or reach out to us at [support@alshival.com](mailto:support@alshival.com) 🌟📩🚀💻

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
<!--         <tr>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-08-04%207.43.52%20AM.png?raw=True" alt="Image Description">
            </td>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-08-04%207.43.58%20AM.png?raw=True" alt="Image Description">
            </td>
        </tr> -->
        <tr>
            <td colspan="2" style="width: 100%;">
                <img src="https://github.com/alshival/gpt4-Discord-Bot/blob/main/app/meta/Screenshot%202023-08-09%204.32.11%20AM.png?raw=True" alt="Data Interpreter">
            </td>
        </tr>
    </table>
</body>

</html>

## Usage

- Use the command prefix `!` to interact with the bot:

  - `!fefe <message>`: Ask Fefe to write code or answer questions.
  - `!datalle`: Attach a .CSV file and ask Fefe to generate charts or maps. Then ask `!fefe` to go over the code with you.
  - `!exeggutor`: (Admin) Exeggute raw python code. Ask `!fefe` to go over the code or any errors with you.
- The bot also includes the following slash commands:
  - `/interpreter <message>`: Use the Discord Interpreter to move files around on your PC or raspberry pi, or to generate financial charts. Then ask `!fefe` to go over the code with you.
  - `/help`: Provides a quick rundown of how to use the app.
  - `/stop_music`: Used to stop music playback in voice channels.

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
