from discord.ext import commands
from .cody import Cody
from .cap import Cap

def setup(bot: commands.Bot):
    bot.add_cog(Cody(bot))
    bot.add_cog(Cap(bot))
    


