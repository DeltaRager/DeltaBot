import discord
from discord.ext import commands

async def kick(garith,message):
    b = message.content
    x = b.split('"')
    del x[0]
    k = discord.Server.get_member(user_id)
    j = message.mentions[0].id
    c = j.k
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** **Reason:** %s " % (c,x))
