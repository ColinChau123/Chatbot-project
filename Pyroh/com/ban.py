import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

##this command bans someone
#@botClient.command(name='ban')
#@commands.has_permissions(ban_members=True)
#async def ban(ctx, member: user., *, reason=None):
    #await member.ban(reason=reason)
    #await ctx.send(f'User {member} has been banned')

#this command unbans someone
#@botClient.command()
#@commands.has_permissions(ban_members=True)
#async def unban(ctx, member: discord.Member, *, reason=None):
    #await member.unban(reason=reason)
    #await ctx.send(f'User {member} has been unbanned')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return