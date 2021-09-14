import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class addRole(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None
 
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addRole(self, ctx, member: discord.Member, *, role):
	    guild = ctx.guild
	    a = discord.utils.get(guild.roles, name=role)
	    await ctx.send(f'Role `{a}` has been added to `{member}`.')
	    await member.add_roles(a)
	
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def removeRole(ctx, member: discord.Member, *, role):
	    arole = discord.utils.get(ctx.message.server.roles, name=role)
	    if arole:
		    await member.remove_roles(role)
		    await ctx.send(f'Role `{role}` has been removed from `{member}`.')
	    else:
		    await ctx.send(f'`{member}` does not currently have the role `{role}`.')

def setup(bot):
    bot.add_cog(addRole(bot))

