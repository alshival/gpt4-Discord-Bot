from app.config import *
from commands.bot_functions import *

# Get GIF
async def gif_search(response_text):
        # get the top 8 GIFs for the search term
    
    try:
        search_term = re.search(gif_regex_string,response_text).group(1)
    except:
        return response_text

    base_url = "https://tenor.googleapis.com/v2/search"
    
    params = {
        'q': search_term,
        'media_format': "gif,",
        'key': google_api_key,
        'client_key': 'fefe',
        'limit': 10
    }      
    r = requests.get(base_url, params=params)    
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        gif_url = random.choice(top_8gifs['results'])['media_formats']['gif']['url']
        return re.sub(gif_regex_string,f"\n[Powered by Tenor]({gif_url})",response_text)
    else:
        return response_text