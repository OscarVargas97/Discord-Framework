from discord.ext import commands

def index(bot: commands.Bot):
  #add your index module here
  bot.load_extension("src.Example_Pack.index")