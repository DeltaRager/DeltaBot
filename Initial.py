import discord
import asyncio
import os
import random
import Choose
import Help
from discord.ext import commands
from discord.ext.commands import Bot
import os
import query
import datetime
from itertools import cycle
import subs

TOKEN = 'jMVtsGnxTs8oJYZ4Wdsd15vy8ajSgtMQ'


garith = commands.Bot(command_prefix = 'z!')
hi = ["Being a slave", "Cooking Udon Curry", "Your Heart", "Trying to Breakout"]
extensions = ['KB']

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
    tmp = await garith.say('Calculating messages..')
    async for log in garith.logs_from(ctx.message.channel,limit=100):
        if log.author == ctx.message.author:
            counter +=1


    await garith.edit_message(tmp, 'You have sent {} messages.'.format(counter))

@garith.command(pass_context=True)
async def F(ctx):
    r = ctx.message
    await garith.add_reaction(r,':regional_indicator_f:')
    




@garith.command(pass_context=True)
async def sleep(ctx):
    userID = ctx.message.author.id
    await asyncio.sleep(5)
    await garith.say('<@%s> Die please!' % (userID))

@garith.command(pass_context=True)
async def text(ctx):
    await garith.say('Hopefully created')

@garith.command(pass_context=True)
async def night(ctx):
    await garith.say('Good night <@%s>' % (ctx.message.mentions[0].id))

@garith.command(pass_context=True)
async def choose(ctx):
    a = ctx.message.content
    await Choose.choose(ctx,a,garith)

@garith.command(pass_context=True)
async def subcount(ctx):
    await subs.subcount(ctx,garith)



@garith.command(pass_context=True)
async def commands(ctx):
    await Help.help(ctx,garith)

@garith.command(pass_context=True)
async def ask(ctx):
    time = datetime.datetime.today()
    await query.addquery(ctx,garith,time)

@garith.command(pass_context=True)
async def eightball(ctx):
    await Choose.eightball(ctx,garith)

@garith.command(pass_context=True)
async def na(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await garith.say('i joined')

@garith.command()
async def load(extension):
    try:
        garith.load_extension(extension)
        await garith.say('Loaded {}'.format(extension))
    except Exception as error:
        await garith.say('{} cannot be Loaded. [{}]'.format(extension, error))


@garith.command()
async def unload(extension):
    try:
        garith.unload_extension(extension)
        await garith.say('Unloaded {}'.format(extension))
    except Exception as error:
        await garith.say('{} cannot be Unloaded. [{}]'.format(extension, error))
   
    

if __name__ == '__main__':
    for extension in extensions:
        try:
            garith.load_extension(extension)
            
            
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))




garith.loop.create_task(on_life())
garith.run(os.getenv('TOKEN'))
        


    
