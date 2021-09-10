import discord
from discord.ext import commands

botClient = commands.Bot(command_prefix='!')

@botClient.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name}")

@botClient.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    arole = discord.utils.get(ctx.message.server.roles, name=mutedRole)
    if arole:
        await member.remove_roles(member, mutedRole)
        await ctx.send(f'`{member}` is has been unmuted.')
    else:
        await ctx.send(f'`{member}` is not currently muted.')


#embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
#embed.add_field(name="reason:", value=reason, inline=False)
#await ctx.send(embed=embed)
