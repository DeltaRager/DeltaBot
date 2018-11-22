import discord
import asyncio
import os
import Choose

garith = discord.Client()

@garith.event
async def on_ready():
    print('System check completed')
    print('Rebooting as')
    print(garith.user.name)
    print(garith.user.id)
    print('------')


@garith.event
async def on_message(message):
    if message.content.startswith('d!test'):
        counter=0
        tmp = await garith.send_message(message.channel, 'Calculating messages..')
        async for log in garith.logs_from(message.channel,limit=100):
            if log.author == message.author:
                counter +=1


        await garith.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('d!sleep'):
        userID = message.author.id
        await asyncio.sleep(5)
        await garith.send_message(message.channel, '<@%s> Die please!' % (userID))

    elif message.content.startswith('d!night '):
        await garith.send_message(message.channel, 'Good night <@%s>' % (message.mentions[0].id))

    elif message.content.startswith('d!choose '):
        Choose.choose(message.content)

garith.run(os.getenv('TOKEN'))
        


    
