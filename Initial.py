import discord
import asyncio
import os
import random
import Choose
import Help
from discord.ext import commands
from discord.ext.commands import Bot

garith = commands.Bot(command_prefix = 'g!')



@garith.event
async def on_ready():
    print('System check completed')
    print('Rebooting as')
    print(garith.user.name)
    print(garith.user.id)
    print('------')




@garith.command()
async def test(message):
    counter=0
    tmp = await garith.send_message(message.channel, 'Calculating messages..')
    async for log in garith.logs_from(message.channel,limit=100):
        if log.author == message.author:
            counter +=1
    await garith.edit_message(tmp, 'You have {} messages.'.format(counter))
    
@garith.command()
async def sleep(message):
    userID = message.author.id
    await asyncio.sleep(5)
    await garith.send_message(message.channel, '<@%s> Die please!' % (userID))

@garith.command()
async def night(message):
    await garith.send_message(message.channel, 'Good night <@%s>' % (message.mentions[0].id))

@garith.command()
async def choose(message):
    a = message.content
    await Choose.choose(a,garith,message)

@garith.command()
async def help(message):
    await Help.help(garith,message)
        

garith.run(os.getenv('TOKEN'))
        


    
