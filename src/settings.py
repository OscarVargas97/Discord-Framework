from discord.ext import commands
import discord
from .index import index
import os

def start():
  
  bot = commands.Bot(command_prefix=os.getenv('PREFIX'), description= os.getenv('DESCRIPTION'))
  
  @bot.event
  async def on_ready():
    print('Ready!')

  #Charge all commands from index.py
  index(bot)

  bot.run(os.getenv('TOKEN'))
