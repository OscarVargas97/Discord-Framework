from discord.ext import commands
from .Drive import index as drive
#from Channel import index as channel

def load(bot):
    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord.")

def chargecogs(bot):
    bot.load_extension("src.Drive.index")

