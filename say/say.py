#Discord Imports
import discord

#Redbot Imports
from redbot.core import commands, checks

__version__ = "1.0.0"
__author__ = "XeonMations"


class Say(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.group()
    @checks.admin_or_permissions(administrator=True)
    async def say(self, ctx, text: str):
        """
        Makes the bot say something.
        """
        try:
            await ctx.send(f"{text}")
        except (ValueError, KeyError, AttributeError):
            await ctx.send("There was an error! Please ask Xeon to fix this.")
    
