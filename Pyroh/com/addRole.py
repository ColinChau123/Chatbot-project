#import discord
#from discord.ext import commands

#botClient = commands.Bot(command_prefix='!')

#@botClient.command()
#@commands.has_permissions(kick_members=True)
#async def addRole(ctx, member: discord.Member, *, role: discord.Role):
   # await member.add_roles(member, role)
   # await ctx.send(f'Role `{role}` has been added to `{member}`.')


#@botClient.command()
#@commands.has_permissions(kick_members=True)
#async def removeRole(ctx, member: discord.Member, *, role: discord.Role):
    #arole = discord.utils.get(ctx.message.server.roles, name=role)
    #if arole:
       # await member.remove_roles(member, role)
     #   await ctx.send(f'Role `{role}` has been removed from `{member}`.')
   # else:
     #   await ctx.send(f'`{member}` does not currently have the role `{role}`.')
