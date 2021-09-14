import discord
from discord.ext import commands

class createChannel(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def createText(self, ctx, *, name):
        guild = ctx.guild
        await guild.create_text_channel(name)
        ctx.send(f'Created new channel named `{name}`.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def createVoice(self, ctx, *, name):
        guild = ctx.guild
        await guild.create_voice_channel(name)
        ctx.send(f'Created new channel named `{name}`.')

def setup(bot):
    bot.add_cog(createChannel(bot))
