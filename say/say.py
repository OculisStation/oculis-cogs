#Discord Imports
import discord

#Redbot Imports
from redbot.core import commands, checks, app_commands

__version__ = "1.0.0"
__author__ = "XeonMations"


class Say(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @app_commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def say(self, interaction: discord.Interaction, text: str):
        """
        Makes the bot say something.
        """
        interaction.channel.send(f"{text}")

