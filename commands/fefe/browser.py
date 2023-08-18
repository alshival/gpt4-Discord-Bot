from app.config import *
from commands.bot_functions import *
from bs4 import BeautifulSoup
import requests

async def get_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

async def get_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

async def browse_urls(text):
    # Excluding tenor 
    urls = re.findall(r'\b((?!https://media.tenor\.com)(?:https?://|www\.)\S+)\b', text)
    if len(urls) > 0:
        for url in urls:
            try:
                url_text = await get_text(url)
                url_text = url_text[0:min(2000,len(url_text))]
                # Substitute the URL with its content in the text
                text = text.replace(url, url_text)
            except Exception as e:
                print(f'error downloading URL [{url}]')
        return text
    else:
        return text

async def browser_response(response_text):
    browse = re.search(browse_regex_string,response_text)
    url = browse.group(1)
    if len(url) > 0:
        try:
            url_text = await browser.get_text(url)
            db = await create_connetion()
            
            url_json = {
                'role':'user',
                'content':f"""
Here is the text from {url}:
{url_text}
"""
                }
            return url_json
        except:
            return None
    else:
        return None
            