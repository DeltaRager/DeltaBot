import discord
import discord.ext from commands

async def kick(garith,message):
    a = message.mentions[0].id
    b = message.content
    x = b.split('"')
    del x[0]
    c = message.author.id
    await garith.kick(a)
    await garith.send_message(message.channel,"**The user:** %s **Was kicked by:** <@%s> **Reason:** %s " % (a,c,x))
