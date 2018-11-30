import random
import discord
from discord.ext import commands

async def choose(ctx,a,garith,message):
    x = a.split(" ")
    del x[0]
    a = [1,2,3]
    f = random.choice(a)
    if (f==1):
        e = random.choice(x)
        await garith.say('I choose **%s** ' % e)
    elif (f==2):
        del x[1]
        e = random.choice(x)
        await garith.say('I choose **%s** ' % e)
    elif (f==3):
        del x[0]
        e = random.choice(x)
        await garith.say('I choose **%s** ' % e)


async def eightball(ctx,garith,message):
    possible = [
        'Nope',
        'Not likely',
        'Too hard to tell',
        'Quite possible',
        'Definitely',
        'Maybe'
        ]
    await garith.say(random.choice(possible)) 
        
    
    
