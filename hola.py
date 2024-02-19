import os
from discord import *
from dotenv import load_dotenv
import urllib.request
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

with open('token.txt') as f:
    TOKEN = f.readline()

client.run(TOKEN)

"""
TEMPLATE

@client.event
async def XXXX(YYYY):
    function here
"""


