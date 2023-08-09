import discord
from discord.ext import commands,tasks
from discord import app_commands
import os
import random
import sys
import subprocess
import io
import re 
import requests
import pandas as pd

discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")

############################################
# openai API config 
############################################
import openai
# Set up the OpenAI API. The key is stored as an environment variable for security reasons.
openai_model = 'gpt-4'
openai.api_key = os.environ.get("OPENAI_API_KEY")


# Used to abide by Discord's 2000 character limit.
async def send_chunks(ctx, text):
    chunk_size = 2000  # Maximum length of each chunk

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    for chunk in chunks:
        await ctx.send(chunk)