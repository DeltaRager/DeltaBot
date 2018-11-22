import random

async def choose(a,garith):
    b,c,d=a.split(" ")
    l = [c,d]
    e = random.choice(l)
    await garith.choose(a.channel,'I choose %s ' % e)
