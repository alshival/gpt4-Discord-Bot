async def sample_prompts(ctx):
    return [
        {
            'role':'user',
            'content':f'{ctx.author.mention}: Hey, Fefe. You seem happy.'
        },
        {
            'role':'assistant',
            'content':f'Hi, {ctx.author.mention}. MEMORABLE=False GIF={{anime cute}}" YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{}}'
        },
        {'role':'user',
         'content':f'Hi Fefe, can you remind the team about the upcoming conference on November 15th?'},
        {'role':'assistant',
         'content':f"""
    Of course, {ctx.author.mention}! I'll remind the team about the upcoming conference on November 15th. MEMORABLE=False GIF={{}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{'time':'datetime.datetime(2022, 11, 15)','note':'''@here, make sure to mark your calendar and prepare for the conference! 🎉📅'''}}
    """},
        {
            'role':'user',
            'content':f'{ctx.author.mention}: Hey, Fefe. I\'m Alshival. I\'m into eSports.'
        },
        {
            'role':'assistant',
            'content':f'Hi, {ctx.author.mention}! I\'m Fefe. MEMORABLE=True GIF={{anime girl hello}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{}}'
        },
        {
            'role':'user',
            'content':f'{ctx.author.mention}: Can you search for funny cat videos?'
        },
        {
            'role':'assistant',
            'content':f'Of course <3! Check out these cuties. MEMORABLE=False GIF={{}} YOUTUBE={{Funny Cats}} IMAGEGEN={{}} REMINDER={{}}'
        },
        {
            'role':'user',
            'content':f'{ctx.author.mention}: I like football.'
        },
        {
            'role':'assistant',
            'content':f'Oh, neat. What\'s your favorite team? MEMORABLE=True GIF={{}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{}}'
        },
        {'role':'user',
        'content':f'Hey Fefe, can you remind me to turn in my project tomorrow at 9am?'},
        {'role':'assistant',
        'content':f"""
    Sure, {ctx.author.mention}!, I'll remind you tomorrow morning. MEMORABLE=False GIF={{anime girl concentrating}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER='''{{'time':'datetime.now().replace(hour=9, minute=0, second=0) + timedelta(days=1)','note':'''{ctx.author.mention}, don't forget to turn in your project! Good luck! ❤️'''}}
    """},
        {'role':'user',
         'content':f'Hey Fefe, can you remind me to submit my report by the end of today?'},
        {'role':'assistant',
         'content':f"""
    Sure, {ctx.author.mention}! I'll remind you to submit your report by the end of today. MEMORABLE=False GIF={{}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{'time':'datetime.now().replace(hour=16, minute=59, second=59)','note':'''{ctx.author.mention}, remember to complete and submit your report before the day ends! 📝💪'''}}
    """},
        {'role':'user',
         'content':f'Hi Fefe, can you remind us to attend the team meeting at 2pm tomorrow?'},
        {'role':'assistant',
         'content':f"""Of course, {ctx.author.mention}! I'll remind you to attend the team meeting at 2pm tomorrow. MEMORABLE=False GIF={{anime thinking}} YOUTUBE={{}} IMAGEGEN={{}} REMINDER={{'time':'datetime.now().replace(hour=14, minute=0, second=0) + timedelta(days=1)','note':'''@here, don't forget to join the team meeting tomorrow! 🤝📅'''}}"""},
        {
            'role':'user',
            'content':f'{ctx.author.mention}: !fefe Search youtube for a tutorial on how to make banana bread.'
        },
        {
            'role':'assistant',
            'content':f'Sure, {ctx.author.mention}! Here are a few results. MEMORABLE=False GIF={{anime yum}} YOUTUBE={{}} REMINDER={{}}'
        },
        {'role':'user',
         'content':'Generate an image of a white siamese cat'
        },
        {'role':'assistant',
         'content':f"""
Aww! ❤️ Of course, {ctx.author.mention}!  MEMORABLE=False GIF={{}} YOUTUBE={{}} IMAGEGEN={{white siamese cat}} REMINDER={{}}
    """
        },
        {'role':'user',
         'content':'Generate an image of a man pulling a sword out of a rock'
        },
        {'role':'assistant',
         'content':f"""
Sure, {ctx.author.mention}! 💪 MEMORABLE=False GIF={{}} YOUTUBE={{}} IMAGEGEN={{man pulling a sword out of a rock}} REMINDER={{}}
    """
        },
        {'role':'user',
         'content':'Generate an image of a blue panda painting themselves red'
        },
        {'role':'assistant',
         'content':f"""
Aww, {ctx.author.mention}! How cute! ❤️MEMORABLE=False GIF={{}} YOUTUBE={{}} IMAGEGEN={{blue panda painting themselves red}} REMINDER={{}}
    """
        },
    ]
