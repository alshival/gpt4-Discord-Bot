from app.config import *
from commands.discord_interpreter import finetune_interpreter
from commands.datalle import finetune_datalle
from commands.bot_functions import *

async def discord_interpreter(interaction,message):
    # Create user directory if it does not exist.
    dir_name = await create_user_dir(interaction.user.name)
    
    py_filename = dir_name + f"{interaction.user.name}.py"
    
    # Check if the directory exists
    if not os.path.exists(dir_name):
        # If the directory does not exist, create it
        os.makedirs(dir_name)
        
    db = await create_connection()
    embed1 = discord.Embed(
            description = message,
            color = discord.Color.purple()
        )
    embed1.set_author(name=f"{interaction.user.name} used the Discord Interpreter",icon_url=interaction.user.avatar)
    
    # Random sample finetune_datalle data.
    datalle_messages = await finetune_datalle.finetune_datalle(interaction.user.name)
    datalle_messages = [[datalle_messages[i],datalle_messages[i+1]] for i in [j for j in range(len(datalle_messages)) if j%2==0]] 
    datalle_messages = random.sample(datalle_messages,6)
    datalle_messages = [item for sublist in datalle_messages for item in sublist]
    # Random sample finetune_interpreter data.
    interpreter_messages = await finetune_interpreter.finetune_interpreter(interaction.user.name)
    interpreter_messages = [[interpreter_messages[i],interpreter_messages[i+1]] for i in [j for j in range(len(interpreter_messages)) if j%2==0]] 
    interpreter_messages = random.sample(interpreter_messages,6)
    interpreter_messages = [item for sublist in interpreter_messages for item in sublist]
    # Combine and random sample again
    messages = interpreter_messages + datalle_messages
    messages = random.sample(messages,8)

    # Pull last few DATALL-E & Interpreter interactions in. So that interpreter can continue processing data from DATALL-E.
    cursor = await db.cursor()
    await cursor.execute("""
    select jsonl
    from (
        select jsonl, timestamp from chat_history
        where channel_id = ?
        and source in ('interpreter','DATALL-E')
        order by timestamp desc
        limit ?
    ) as subquery
    order by timestamp asc
    """,(interaction.channel_id,2))
    # Fetch and load the json data from the selected rows
    rows = await cursor.fetchall()
    past_code = []
    for row in rows:
        json_data = json.loads(row[0])
        past_code.append(json_data)
    
    messages.extend(past_code)

    messages.append({'role': 'user', 'content': message})
    
    messages = check_tokens(messages,model = openai_model,completion_limit = data_viz_completion_limit)

    try:
        response = openai.ChatCompletion.create(
            model=openai_model,
            messages=messages,
            max_tokens=data_viz_completion_limit,
            n=1,
            temperature=0.6,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            user = interaction.user.name
        )
    except Exception as e:
        m = f'''
I ran into an Error: 
```
{type(e).__name__} - {str(e)}
```

Here's the code:

```
{extracted_code}
```
'''    
        jsonl = {'role':'user','content':m}
        with open(py_filename, 'w') as file:
            file.write(m)
            
        await send_interactions(f"Mmm. I tried something, but it didn't work. Take a look at the error file and ask again or ask Fefe for assistance.",file = discord.File(py_filename),embed=embed1)
        
        
    response_text = response['choices'][0]['message']['content']
    
    if '`' in response_text:
        extracted_code = extract_code(response_text)
    elif 'import' in response_text:
        extracted_code = response_text
    else:
        extracted_code = response_text
        print("No code found")
        
    vars = {}
    # Save the original stdout so we can reset it later
    original_stdout = sys.stdout
    # Create a StringIO object to capture output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output
    
    try:
        response_compiled = compile(extracted_code,"<string>","exec")
        exec(response_compiled, vars,vars)
        sys.stdout = original_stdout
        output = captured_output.getvalue()
        m = f'''
################################################################
Fine-tuning:
################################################################
{{'role':'user','content':"""{r'' +message}"""}},
{{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
        jsonl = {'role':'user','content':message}
        # Send the zcode back to the user
        with open(py_filename, 'w') as file:
            file.write(m)
            
        # Gather files to send
        files_to_send = await gather_files_to_send(interaction.user.name)
        # Send the .png file back
        await send_followups(interaction,f'''
output: \n
```
{output}
```
    ''',files=files_to_send,embed=embed1)
            
        await store_prompt(db,json.dumps(jsonl),interaction.channel_id,interaction.channel.name,'interpreter')
        await store_prompt(db,json.dumps({'role':'assistant','content':extracted_code}),interaction.channel_id,interaction.channel.name,'interpreter')
        await db.close()
        await delete_files(interaction.user.name)
    except Exception as e:
        print(message)
        print(e)
        print(extracted_code)
        m = f'''
I ran into an Error: 
```
{type(e).__name__} - {str(e)}
```

Here's the code:

```
{extracted_code}
```
'''
        jsonl = {'role':'user','content':m}
        with open(py_filename, "w") as file:
            file.write(m)
        await interaction.followup.send("I ran into an error.",files = [discord.File(py_filename)],embed=embed1)
        sys.stdout = original_stdout
        
        await store_prompt(db,json.dumps(jsonl),interaction.channel_id,interaction.channel.name,'interpreter')
        await store_prompt(db,json.dumps({'role':'assistant','content':'noted'}),interaction.channel_id,interaction.channel.name,'interpreter')
        await db.close()
        await delete_files(interaction.user.name)
        return
        