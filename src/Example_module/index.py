from discord.ext import commands
from .pong_example import PongCommands
from .ping_example import PingCommands

def setup(bot: commands.Bot):
    bot.add_cog(PongCommands(bot))
    bot.add_cog(PingCommands(bot))
    


