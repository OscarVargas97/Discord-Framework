from discord.ext import commands

class PongCommands(commands.Cog, name="PongCommands"):
  """Receives ping commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def pong(self, ctx: commands.Context):
    """Checks for a response from the bot"""
    await ctx.send("Pong")

  @commands.command()
  async def ultrapong(self, ctx: commands.Context):
    """Checks for a response from the bot"""
    await ctx.send("Ultra Pong")
