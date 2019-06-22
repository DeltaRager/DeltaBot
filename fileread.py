import discord
from discord.ext import commands


async def text(ctx):
        f= open("itworks.txt","w+")
        for i in range(10):
                f.write("This is line %d\r\n" % (i+1))
        f.close()
