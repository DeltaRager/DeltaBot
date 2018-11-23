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


garith = discord.Client()



@garith.event
async def on_ready():
    print('System check completed :c')
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

    elif message.content.startswith('g!help'):
        await Help.help(garith,message)


    elif message.content.startswith('g!cchar'):
        with open ('users.json', 'r') as f:
            users = json.load(f)

        a = message.content
        name,age,gend,des = a.split(" ")
        await add_charname(users, name)
        await add_charage(users, age)
        await add_chargender(users, gend)
        await add_chardesc(users, des)
        
        with open('users.json', 'w') as f:
            json.dump(users, f)

async def add_charname(users, name):
    if not name in users:
        users[name]['Name'] = {}

async def add_charage(users, age):
    users[age]['Age']={}

async def add_chargender(users, gend):
    users[gend]['Gender']={}

async def add_chardesc(users, des):
    users[des]['Description'] = {}
          


         
        

garith.run(os.getenv('TOKEN'))
        


    
