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


garith = commands.Bot(command_prefix = 'g!')
hi = ["Being a slave", "Cooking Ramen", "Your Heart", "Trying to Breakout"]

@garith.event
async def on_ready():
    print('System check completed :c')
    print('Rebooting as')
    print(garith.user.name)
    print(garith.user.id)
    print('------')

async def on_life():
    await garith.wait_until_ready()
    status = cycle(hi)

    while not garith.is_closed:
        current = next(status)
        await garith.change_presence(game=discord.Game(name=current))
        await asyncio.sleep(90)




@garith.command(pass_context=True)
async def test(ctx):
    counter=0
    tmp = await garith.send_message(message.channel, 'Calculating messages..')
    async for log in garith.logs_from(message.channel,limit=100):
        if log.author == ctx.message.author:
            counter +=1


    await garith.edit_message(tmp, 'You have sent {} messages.'.format(counter))


@garith.command(pass_context=True)
async def sleep(ctx):
    userID = ctx.message.author.id
    await asyncio.sleep(5)
    await garith.say('<@%s> Die please!' % (userID))

@garith.command(pass_context=True)
async def night(ctx):
    await garith.say('Good night <@%s>' % (ctx.message.mentions[0].id))

@garith.command(pass_context=True)
async def choose(ctx):
    a = ctx.message.content
    await Choose.choose(ctx,a,garith,message)

@garith.command(pass_context=True)
async def help(ctx):
    await Help.help(ctx,garith,message)

@garith.command(pass_context=True)
async def ask(ctx):
    time = datetime.datetime.today()
    await query.addquery(ctx,garith,message,time)

@garith.command(pass_context=True)
async def 8ball(ctx):
    await Choose.eightball(ctx,garith,message)


    


         
        
garith.loop.create_task(on_life())
garith.run(os.getenv('TOKEN'))
        


    
