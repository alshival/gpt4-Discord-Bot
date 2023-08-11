from app.config import *
from commands.discord_interpreter import finetune
from commands.bot_functions import *

async def discord_interpreter(interaction,message):
    db = await create_connection()
    embed1 = discord.Embed(
            description = message,
            color = discord.Color.purple()
        )
    embed1.set_author(name=f"{interaction.user.name} used the Discord Interpreter",icon_url=interaction.user.avatar)
    py_filename = f"app/downloads/{interaction.user.name}.py"
    
    messages = [[finetune.finetune[i],finetune.finetune[i+1]] for i in [j for j in range(len(finetune.finetune)) if j%2==0]] 

    # Random sample messages.
    messages = random.sample(messages,5)
    # sample_stock_charts defined in `app/config.py`.

    messages = [item for sublist in messages for item in sublist]

    # Pull last 2 DATALL-E & Interpreter interactions in. So that interpreter can continue processing data from DATALL-E.
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
    """,(interaction.channel_id,4))
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
        return
        
    sys.stdout = original_stdout
    output = captured_output.getvalue()
    m = f'''
################################################################
Fine-tuning:
################################################################
{{'role':'user','content':"""{r'' +message}"""}},
{{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
    jsonl = {'role':'user','content':message}
    strings =  [x for x in vars.values() if (type(x) is str)]
    files_to_send = [x  for x in strings if re.search("^app/downloads/.+\/?.+\.[a-zA-Z0-9]+$",x) is not None]
    files_to_send = [x for x in files_to_send if file_size_ok(x)==True]
    # Send the zcode back to the user
    with open(py_filename, 'w') as file:
        file.write(m)
    # Send the .png file back
    await interaction.followup.send(f'''
```
{output}
```
''',files=[discord.File(x) for x in files_to_send] + [discord.File(py_filename)],embed=embed1)
        
    await store_prompt(db,json.dumps(jsonl),interaction.channel_id,interaction.channel.name,'interpreter')
    await store_prompt(db,json.dumps({'role':'assistant','content':extracted_code}),interaction.channel_id,interaction.channel.name,'interpreter')
    await db.close()