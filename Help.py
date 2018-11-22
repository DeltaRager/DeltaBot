import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands


async def help(garith,message):
    await garith.send_message(message.channel,"**Ze Commands** \n```Prefix: 'g!'\n------ \n\n1.help\n----\nInfo:Gives you the juicy commands\n\n2.test\n----\nInfo:Counts the number of messsages you have sent\n\n3.sleep\n-----\nInfo:Gives you a message filled with kindness\n\n4.night <user>\n------------\nInfo:The bot tells the given user good night\n\n5.choose <options>\n------\nInfo:The Bot chooses between the options provided(leave a space after every option)```")
    
