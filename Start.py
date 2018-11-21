import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Alive as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('d!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('d!sleep'):
        userID= message.author.id     
        await asyncio.sleep(5)
        await client.send_message(message.channel, '<@%s> Die please!' % (userID))

    elif message.content.startswith('d!night' ):
        await client.send_message(message.channel, "Good night <@%s> " % (message.mentions[0].id))
        

client.run('NTE0NzI2NjE3OTU2ODc2Mjg4.Dtconw.getv698Q4iB_P99GZPfsTvTQuxk')
