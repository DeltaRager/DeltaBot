import random
import os
import discord
import asyncio

garith = discord.Client()

@garith.event
async def choose(a):
    b,c,d=a.split(" ")
    l = [c,d]
    e = random.choice(l)
    await garith.choose(message.channel,'I choose *%s* ' % e)

