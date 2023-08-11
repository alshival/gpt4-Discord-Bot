from app.config import *
from commands.bot_functions import *

      
async def Exeggute(ctx,python):
    embed1 = discord.Embed(
            color = discord.Color.dark_red()
        )
    embed1.set_author(name=f"{ctx.author.name} used the Exeggutor",icon_url=ctx.message.author.avatar)


    
    vars = {}
    # Save the original stdout so we can reset it later
    original_stdout = sys.stdout
    # Create a StringIO object to capture output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output

    try:
        extracted_code = extract_code(python) # Extract the code
        code_compiled = compile(extracted_code,"<string>","exec") # Compiling code

        exec(code_compiled,vars,vars)  # execute the code    
    except Exception as e:
        m = f"""
Here's the error:
```
{type(e).__name__} - {e}
```
and here's the code:
```
{extracted_code}
```
"""
        pack = {"role":"user","content":m}
        await send_results(ctx,m,embed1)
        print(f"Error: {type(e).__name__} - {e}")
        sys.stdout = original_stdout
        db = await create_connection()
        await store_prompt(db,json.dumps(pack),ctx.channel.id,ctx.channel.name,'exeggutor')
        await store_prompt(db,json.dumps({"role":"assistant","content":"Noted"}),ctx.channel.id,ctx.channel.name,'exeggutor')
        await db.close()
        return
    sys.stdout = original_stdout
    # Get the output
    output = captured_output.getvalue()
    print("done exegguting")
    jsonl = f'''
```
{output}
```
'''
    # check if there are any files
    strings =  [x for x in vars.values() if (type(x) is str)]
    files_to_send = [x  for x in strings if re.search("^app/downloads/.+\/?.+\.[a-zA-Z0-9]+$",x) is not None]
    files_to_send = [x for x in files_to_send if file_size_ok(x)==True]
    #send results
    await send_results(ctx,output,embed1,files_to_send)
    
    db = await create_connection()
    m = f"""
Here's my code:
```
{extracted_code}
```
and here's the output:
```
{output}
```
"""
    
    pack = {'role':'user','content':m}
    await store_prompt(db,json.dumps(pack),ctx.channel.id,ctx.channel.name,'exeggutor')
    await store_prompt(db,json.dumps({'role':'assistant','content':'Noted'}),ctx.channel.id,ctx.channel.name,'exeggutor')
    await db.close()