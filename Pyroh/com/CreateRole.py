import discord
from discord.ext import commands

class createRole(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def createRole(self, ctx, role: discord.Role):
	    guild = ctx.guild
	    await guild.create_role(name=role)
	    await ctx.send(f'Role `{role}` has been created')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def deleteRole(self, ctx, *, role):
	    guild = ctx.guild
	    arole = discord.utils.get(ctx.message.server.roles, name=role)
	    if arole:
		    await guild.delete_role(ctx.message.server, role)
		    await ctx.channel.send(f'The role `{role}` has been deleted.')
	    else:
		    await ctx.send(f'The role doesn\'t exist.')

def setup(bot):
    bot.add_cog(createRole(bot))

