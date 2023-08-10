from app.config import *
import openai
import aioduckdb

# Create database 
async def create_connection():
    return await aioduckdb.connect('app/data.db')

async def create_chat_history_table():
    db = await create_connection()
    cursor = await db.cursor()
    await cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history
    (username TEXT NOT NULL,
    prompt TEXT NOT NULL,
    model TEXT,
    response TEXT,
    channel_id TEXT,
    channel_name TEXT,
    source TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """)
    await db.commit()
    await db.close()

# Function to store a prompt
async def store_prompt(db_conn,username,prompt,model,response,channel_id,channel_name,source):
    cursor = await db_conn.cursor()
    await cursor.execute("""
INSERT INTO chat_history (username,prompt,model,response,channel_id,channel_name,source) VALUES (?,?,?,?,?,?,?) 
""",(username,prompt,model,response,channel_id,channel_name,source))
    await db_conn.commit()
    
# Function to fetch the last few prompts. Used to provide chat history to openAi.
async def fetch_prompts(db_conn, channel_id, limit):
    async with db_conn.cursor() as cursor:
        query = """
        SELECT prompt, response 
        FROM (
            SELECT prompt, response, timestamp 
            FROM chat_history 
            WHERE channel_id = ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        ) AS subquery 
        ORDER BY timestamp ASC;
        """
        
        await cursor.execute(query, (channel_id, limit,))
        return await cursor.fetchall()

# Get list of channels
async def list_channels(bot):
    channel_names = []
    for guild in bot.guilds:
        for channel in guild.channels:
            channel_names.append(channel.name)
    return channel_names

# Get first text channel
async def get_first_text_channel(bot):
    for guild in bot.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):  # If you want text channels only
                return channel
    return None
############################################
# Useful Functions
############################################
# Code used to strip commentary from GPT response.
def extract_code(response_text):
    pattern = pattern = r"```(?:[a-z]*\s*)?(.*?)```\s*"
    match = re.search(pattern, response_text, re.DOTALL)
    if match:
        extracted_code = match.group(1) # Get the content between the tags\n",
    elif 'import' in response_text:
        extracted_code = response_text
    else:
        extracted_code = response_text
        print("No code found.")
    return extracted_code

# Function to send response in chunks. Used to adhere to discord's 2000 character limit.
async def send_results(ctx, output, embed=None, files_to_send=[]):
    chunk_size = 2000  # Maximum length of each chunk
    
    response = f'''
```
{output}
```'''
    
    chunks = [response[i:i+chunk_size] for i in range(0, len(response), chunk_size)]
    
    if len(chunks) == 1:
        if embed:
            await ctx.send(chunks[0],files = [discord.File(x) for x in files_to_send],embed=embed)
        else:
            await ctx.send(chunks[0],files = [discord.File(x) for x in files_to_send])
    else:
        for chunk in chunks:
            if chunk != chunks[len(chunks)-1]:
                await ctx.send(chunk)
            else:
                if embed:
                    await ctx.send(chunk,files = [discord.File(x) for x in files_to_send])
                else: 
                    await ctx.send(chunk,files = [discord.File(x) for x in files_to_send],embed=embed)

# Function to clear the downloads folder
async def delete_music_downloads(bot):
    def delete_everything(directory):
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_everything(file_path)
                os.rmdir(file_path)
    
    directory = 'app/downloads'
    if os.path.exists(directory) and os.path.isdir(directory):
        delete_everything(directory)

# Check tokens
def check_tokens(jsonl, model,completion_limit):
    enc = tiktoken.encoding_for_model(model)
    messages_string = json.dumps(jsonl)
    tokens = len(enc.encode(messages_string))

    if model == 'gpt-3.5-turbo':
        token_limit = 4096
    if model == 'gpt-4':
        token_limit = 8000
    
    while tokens > token_limit - completion_limit:
        # Remove the first two messages from the JSON list
        jsonl = jsonl[2:]
        
        # Update the messages string and token count
        messages_string = json.dumps(jsonl)
        tokens = len(enc.encode(messages_string))
    
    return jsonl
# Used to abide by Discord's 2000 character limit.
async def send_chunks(ctx, text):
    chunk_size = 2000  # Maximum length of each chunk

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    for chunk in chunks:
        await ctx.send(chunk)