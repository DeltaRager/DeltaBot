import discord
import asyncio
import os
import random
import Choose
from discord.ext import commands
from discord.ext.commands import Bot


garith = discord.Client()

Garith = commands.bot( command_prefix=('g!','G!'))

@garith.event
async def on_ready():
    print('System check completed')
    print('Rebooting as')
    print(garith.user.name)
    print(garith.user.id)
    print('------')


@garith.event
async def on_message(message):
    if message.content.startswith('g!test'):
        counter=0
        tmp = await garith.send_message(message.channel, 'Calculating messages..')
        async for log in garith.logs_from(message.channel,limit=100):
            if log.author == message.author:
                counter +=1


        await garith.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('g!sleep'):
        userID = message.author.id
        await asyncio.sleep(5)
        await garith.send_message(message.channel, '<@%s> Die please!' % (userID))

    elif message.content.startswith('g!night '):
        await garith.send_message(message.channel, 'Good night <@%s>' % (message.mentions[0].id))

    elif message.content.startswith('g!choose '):
        a = message.content
        await Choose.choose(a,garith,message)

@Garith.command()
async def test(ctx):
    await ctx.send('123 check, works fine')

        

garith.run(os.getenv('TOKEN'))
        


    
