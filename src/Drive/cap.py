from discord.ext import commands

class Cap(commands.Cog, name="Cap"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def pung(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("Ping")
