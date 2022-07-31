from discord.ext import commands

class PingCommands(commands.Cog, name="PingCommands"):
  """Receives ping commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx: commands.Context):
    """Checks for a response from the bot"""
    await ctx.send("Ping")

  @commands.command()
  async def ultraping(self, ctx: commands.Context):
    """Checks for a response from the bot"""
    await ctx.send("Ultra Ping")
