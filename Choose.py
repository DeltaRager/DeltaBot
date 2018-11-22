import discord
import asyncio

@garith.event
async def on_message(message):
    if message.content.startswith('d!choose'):
        a = message.content
        b,c,d = a.split(" ")
        print(a,b,c,d)
        
