import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author ==client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message1(message):
    if message.author ==client.user:
        return
    
    if message.content.startswith('$axel'):
        await message.channel.send('https://cdn.discordapp.com/attachments/1046647124655345706/1127798411790401608/SPOILER_67e1f5e72fb3ec6b98be0794e601d472.mp4?ex=65e53b1e&is=65d2c61e&hm=e6e4acf7509f7a23c8a8be57b7ba755e1afeb8e5f1ced3f3c6e597c4dae4eacf&')

@client.event
async def on_message2(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$ping'):
        await message.channel.send('pong!')


"""
TEMPLATE

@client.event
async def XXXX(YYYY):
    function here
"""

with open('token.txt') as f:
    TOKEN = f.readline()

client.run(TOKEN)