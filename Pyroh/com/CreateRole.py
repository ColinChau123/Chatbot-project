import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

@botClient.command()
@commands.has_permissions(manage_roles=True)
async def createRole(ctx, role: discord.Role):
	guild = ctx.guild
	await guild.create_role(name=role)
	await ctx.send(f'Role `{role}` has been created')

@botClient.command()
@commands.has_permissions(manage_roles=True)
async def deleteRole(ctx, *, role):
	arole = discord.utils.get(ctx.message.server.roles, name=role)
	if arole:
		await botClient.delete_role(ctx.message.server, role)
		await ctx.channel.send(f'The role `{role}` has been deleted.')
	else:
		await ctx.send(f'The role doesn\'t exist.')
