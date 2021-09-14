import discord
from discord.ext import commands

class Kick(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):    
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

def setup(bot):
    bot.add_cog(Kick(bot))
