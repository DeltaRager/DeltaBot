import random
import os
import discord
import asyncio

async def choose(a):
    b,c,d=a.split(" ")
    l = [c,d]
    e = random.choice(l)
    await garith.send_message(message.channel,'I choose *%s* ' % e)

