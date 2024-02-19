import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv("")

bot = commands.Bot(command_prefix="-")

"""
TEMPLATE

@bot.command(name="xxxxxx")
async def xxxxx ()"""

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")