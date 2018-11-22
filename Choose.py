import random
import discord

async def choose(a,garith,message):
    b,c,d,e,f,g,h,i,j=a.split(" ")
    l = [c,d,e,f,g,h,i,j]
    e = random.choice(l)
    await garith.send_message(message.channel,'I choose %s ' % e)
