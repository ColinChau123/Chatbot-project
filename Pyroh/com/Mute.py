import discord
from discord.ext import commands

class Mute(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"You have been muted from: {guild.name}")
        await ctx.send(f'`{member}` is has been muted.')
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        
        if member.has_role(mutedRole):
            await member.remove_roles(mutedRole, reason=reason)
            await member.send(f"You have been unmuted from: {guild.name}")
            await ctx.send(f'`{member}` is has been unmuted.')
        else:
            await ctx.send(f'`{member}` is not currently muted.')

def setup(bot):
    bot.add_cog(Mute(bot))


#embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
#embed.add_field(name="reason:", value=reason, inline=False)
#await ctx.send(embed=embed)
