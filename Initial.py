import discord
import asyncio
import os
import random
import Choose
import Help
from discord.ext import commands
from discord.ext.commands import Bot
import json
import os
import query
import datetime
from itertools import cycle


garith = discord.Client()

hi = ["Being a slave", "Cooking Ramen", "Your Heart", "Trying to Breakout"]

@garith.event
async def on_ready():
    print('System check completed :c')
    print('Rebooting as')
    print(garith.user.name)
    print(garith.user.id)
    print('------')

async def on_life():
    await client.wait_until_ready()
    status = cycle(hi)

    while not garith.is_closed:
        current = next(status)
        await garith.change_presence(game=discord.Game(name=current))
        await asyncio.sleep(90)




@garith.event
async def on_message(message):
    if message.content.startswith('g!test'):
        counter=0
        tmp = await garith.send_message(message.channel, 'Calculating messages..')
        async for log in garith.logs_from(message.channel,limit=100):
            if log.author == message.author:
                counter +=1


        await garith.edit_message(tmp, 'You have sent {} messages.'.format(counter))
    elif message.content.startswith('g!sleep'):
        userID = message.author.id
        await asyncio.sleep(5)
        await garith.send_message(message.channel, '<@%s> Die please!' % (userID))

    elif message.content.startswith('g!night '):
        await garith.send_message(message.channel, 'Good night <@%s>' % (message.mentions[0].id))

    elif message.content.startswith('g!choose '):
        a = message.content
        await Choose.choose(a,garith,message)

    elif message.content.startswith('g!help'):
        await Help.help(garith,message)

    elif message.content.startswith('g!ask'):
        time = datetime.datetime.today()
        await query.addquery(garith,message,time)


    


         
        
garith.loop.create_task(on_life())
garith.run(os.getenv('TOKEN'))
        


    
