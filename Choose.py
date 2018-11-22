import random
import discord

async def choose(a,garith,message):
    x = a.split(" ")
    del x[0]
    e = random.choice(x)
    await garith.send_message(message.channel,'I choose **%s** ' % e)
