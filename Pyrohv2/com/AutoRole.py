import discord
from discord.ext import commands

class autorole(commands.Cog):
    """Automatically assign roles to new members on join."""

    def init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        """when person joins, it gets the role member"""
        guild = ctx.guild
        memberRole = discord.utils.get(guild.roles, name="Member")
        await member.add_roles(memberRole)

    @commands.Cog.listener()
    async def on_server_join(self, ctx):
        """Adds the role members were supposed to get when the bot joins"""
        guild = ctx.guild
        role = discord.utils.get(ctx.guild.roles, name="Member")
        adminRole = discord.utils.get(ctx.guild.roles, name="Admin")
        if not role:
            role = await guild.create_role(name="Member")
            for channel in guild.channels:
                await channel.set_permissions(role, speak=True, send_messages=True, read_message_history=True, read_messages=False)
        
        if not adminRole:
            adminRole = await guild.create_role(name="Admin")
            for channel in guild.channels:
                await channel.set_permissions(adminRole, speak=True, send_messages=True, read_message_history=True, read_messages=True)

        for m in ctx.message.server.members:
            if m.has_role(role):
                try:
                    await m.add_roles(role)
                except discord.Forbidden:
                    await self.bot.say("I am not allowed to add roles.")
                    return

def setup(bot):
    bot.add_cog(autorole(bot))