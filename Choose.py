import random
import discord

async def choose(a,garith,message):
    b,c,d=a.split(" ")
    l = [c,d]
    e = random.choice(l)
    await garith.send_message(message.channel,'I choose %s ' % e)
