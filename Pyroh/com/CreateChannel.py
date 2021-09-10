import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

@botClient.command()
@commands.has_permissions(kick_members=True)
async def createText(ctx, *, name):
    guild = ctx.guild
    await guild.create_text_channel(name)
    ctx.send(f'Created new channel named `{name}`.')

@botClient.command()
@commands.has_permissions(kick_members=True)
async def createVoice(ctx, *, name):
    guild = ctx.guild
    for channel in guild.channels:
        if (channel.name == name):
            await channel.delete()
