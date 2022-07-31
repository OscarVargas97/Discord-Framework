from discord.ext import commands
from .ready import Ready
#from Channel import index as channel

def chargecogs(bot):
    bot.add_cog(Ready(bot))
    bot.load_extension(".Example_module.index")

