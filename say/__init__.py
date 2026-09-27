from .say import say

async def setup(bot):
    await bot.add_cog(say(bot))
