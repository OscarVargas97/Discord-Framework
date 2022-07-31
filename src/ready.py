from discord.ext import commands

class Cap(commands.Cog, name="Ready"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.event()
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord.")