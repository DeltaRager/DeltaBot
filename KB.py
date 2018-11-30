import discord
from discord.ext import commands

async def kick(garith,message):
    a = message.mentions[0].mention
    b = message.content
    x = b.split('"')
    del x[0]
    await garith.kick(a)
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** **Reason:** %s " % (a,x))
