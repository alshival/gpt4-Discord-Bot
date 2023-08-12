from app.config import *
from commands.bot_functions import *

async def search_youtube(message):
    try:
        search_response = youtube.search().list(
            q = message,
            part = "id,snippet",
            maxResults = 3
        ).execute()
        
        # Create a formatted string with the video titles
        video_title = [f"""[{search_result["snippet"]["title"]}](https://www.youtube.com/watch?v={search_result["id"]["videoId"]})""" for search_result in search_response.get("items",[]) if search_result["id"]["kind"]=="youtube#video"]
        
        video_titles = "\n".join(
            f"""[{search_result["snippet"]["title"]}](https://www.youtube.com/watch?v={search_result["id"]["videoId"]})"""
            for search_result in search_response.get("items", [])
            if search_result["id"]["kind"] == "youtube#video"
        )
        
        return video_title[0]

    except HttpError as e:
        await interaction.followup.send(f"Sorry, there appears to have been an issue while searching: \n \n{e}")
        print("An HTTP error occurred:")
        print(e)
