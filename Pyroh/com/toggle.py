import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

@botClient.command()
@commands.has_permissions(kick_members=True)
async def toggle():
    print("btoggle has been switched")
    global bToggle
    bToggle = not bToggle