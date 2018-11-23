import discord
from discord.ext import commands
import youtube_dl
import nacl.secret

players = {}

async def join(garith,message):
    channel = message.author.voice.voice_channel
    await garith.join_voice_channel(channel)
    
async def leave(garith,message):
    server = message.server
    voice_garith = garith.voice_garith_in(server)
    await voice_garith.disconnect()

async def play(garith,message):
    a = message.content
    b,url = a.split(" ")
    await garith.join_voice_channel(message.author.voice.voice_channel)
    server = message.server
    voice_garith = garith.voice_client_in(server)
    player = await voice_garith.create_ytdl_player(url)
    players[server.id] = player
    player.start()
