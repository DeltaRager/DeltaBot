import discord
from discord.ext import commands

async def kick(garith,message):
    b = message.content
    x = b.split('"')
    del x[0]
    await garith.kick(message.mentions[0].mention)
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** **Reason:** %s " % (message.mentions[0].mention,x))
