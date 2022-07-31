from discord.ext import commands
#add your modules here
from .pong_example import PongCommands
from .ping_example import PingCommands

def setup(bot: commands.Bot):
  #add commands from yours 
  bot.add_cog(PongCommands(bot))
  bot.add_cog(PingCommands(bot))


