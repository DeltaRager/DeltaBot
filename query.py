import discord
from discord.ext import commands
import asyncio
from datetime import date, datetime, timedelta
import sys

async def addquery(garith,message,time):
    name = message.author.name
    question = message.content
    a,b=question.split("/")
    date = time.strftime("%H:%M")
    await garith.send_message(message.channel,'Successfully submitted query!')
    channel = discord.Object(id='516566401188888596')
    await garith.send_message(channel, '**The user:** %s **asked:** %s **at** %s' % (name,b,date))
    
    
    
    
