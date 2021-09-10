import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

@botClient.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')
