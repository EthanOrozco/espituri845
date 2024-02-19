import discord

intents = discord.Intents.default()
intents.message_content = True
<<<<<<< HEAD

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

client.run('OTQyMjc4NTk2NDEwNjM4Mzc2.G42NFz.a3jVS2iXuGDcNReBF8aHT8pcHs-bIeu8iwLorU')
=======

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


>>>>>>> f79dfcf390694f631e83ec1d4479a77263775a15
