import discord
from discord.ext import commands

async def join(garith,message):
    channel = message.author.voice.voice_channel
    await garith.join_voice_channel(channel)
    
async def leave(garith,mesage):
    server = message.server
    voice_garith = garith.voice_garith_in(server)
    await voice_garith.disconnect()
