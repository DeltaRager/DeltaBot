import discord
from discord.ext import commands

async def join(graith,message,ctx):
    channel = ctx.message.author.voice.voice_channel
    await garith.join_voice_channel(channel)
    
