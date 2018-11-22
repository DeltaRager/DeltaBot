import random
import discord

async def choose(garith,message):
    n = int(input("Enter the number of choices: ")
    for x in range(n):
            x = input("")
            try:  
                the_list.append(int(x))
            except ValueError:
                the_list.append(x)
    e = random.choice(x)
    await garith.send_message(message.channel,'I choose %s ' % e)
