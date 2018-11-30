import discord
from discord.ext import commands

async def kick(garith,message):
    b = message.content
    x = b.split('"')
    del x[0]
    a = discord.Server.get_member(message.mentions[0].id)
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** **Reason:** %s " % (a,x))
