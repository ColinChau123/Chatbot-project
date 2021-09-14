import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned.")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        banned_users = await  ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:            
            user = ban_entry.user
            

            if (user.name, user.discriminator) == (member_name, member_discriminator, user_id):
                await ctx.guild.unban(user)
                await ctx.send(f"{user} has been unbanned.")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def multi_ban(memberList):
        for member in memberList:
            await member.ban()
            await ctx.send(f"{member} has been banned.")
            


def setup(client):
    client.add_cog(Ban(client))