import discord
from discord.ext import commands
import asyncio
from datetime import date, datetime, timedelta
import sys

async def addquery(ctx,garith,time):
    name = ctx.message.author.name
    question = ctx.message.content
    origin = ctx.message.channel
    a,b=question.split("/")
    date = time.strftime("%H:%M")
    await garith.say('Successfully submitted query!')
    channel = discord.Object(id='516566401188888596')
    await garith.send_message(channel, '**The user:** %s **asked:** %s **from the channel:** %s' % (name,b,origin))
    
    
    
    
