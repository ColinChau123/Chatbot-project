import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

#this command bans someone
@botClient.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')

#this command unbans someone
@botClient.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'User {member} has been unbanned')
