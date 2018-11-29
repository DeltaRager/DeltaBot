import random
import discord

async def choose(a,garith,message):
    x = a.split(" ")
    del x[0]
    a = [1,2,3]
    f = random.choice(a)
    if (a==1):
        e = random.choice(x)
    elif (a==2):
        del x[1]
        e = random.choice(x)
    elif (a==3):
        del x[0]
        e = random.choice(x)
        
    
    await garith.send_message(message.channel,'I choose **%s** ' % e)
