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
import json

discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")

############################################
# openai API config 
############################################
import openai
import tiktoken
# Set up the OpenAI API. The key is stored as an environment variable for security reasons.
openai_model = 'gpt-4'
# Abide to token limit:
data_viz_completion_limit = 1500
openai.api_key = os.environ.get("OPENAI_API_KEY")

############################################
# GIFY API config 
############################################
gify_api_token = os.environ.get("GIPHY_API_KEY")