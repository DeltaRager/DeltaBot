import discord
from discord.ext import commands

async def kick(garith,message,user: discord.Member):
    b = message.content
    x = b.split('"')
    del x[0]
    await garith.kick(user)
    await garith.send_message(message.channel,"**The user:** <@%s> **Was kicked by:** **Reason:** %s " % (message.mentions[0].id,x))
