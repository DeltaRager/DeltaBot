import discord
from discord.ext import commands

async def kick(garith,message):
    b = message.content
    x = b.split('"')
    del x[0]
    user_id = message.mentions[0].id
    k = discord.Server.get_member(user_id)
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** **Reason:** %s " % (k,x))
