import discord
from discord.ext import commands


class admin:
    def __init__(self,garith):
        self.garith = garith

    @commands.command()
    async def kick(self,message,user: discord.Member):
        a = ctx.message.content
        b = a.split('-')
        del b[0]
        c = b[0]
        await self.garith.kick(userName)
        await self.garith.say("%s **was kicked, reason:** %s" % (userName,c))

def setup(garith):
    garith.add_cog(admin(garith))
