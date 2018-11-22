import random
import discord

async def choose(garith,message):
    print("Enter the size of the list:")
    N = input()
    for x in range(N):
            x = input("")
            try:  
                the_list.append(int(x))
            except ValueError:
                the_list.append(x)
    e = random.choice(x)
    await garith.send_message(message.channel,'I choose %s ' % e)
