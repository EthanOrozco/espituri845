import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv("OTQyMjc4NTk2NDEwNjM4Mzc2.GR1iPj.GSddEA0JrLUa_uiP4-yhPzPwwrHI1eIuL_Gyjw")

bot = commands.Bot(command_prefix="-")

"""@bot.command(name="xxxxxx")
async def xxxxx ()"""
