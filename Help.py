import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands


async def help(ctx,garith):
    await garith.say("**Ze Commands** \n```Prefix: 'g!'\n------ \n\n1.help\n------\nInfo:Gives you the juicy commands\n\n2.test\n------\nInfo:Counts the number of messsages you have sent\n\n3.sleep\n-------\nInfo:Gives you a message filled with kindness\n\n4.night <user>\n--------------\nInfo:The bot tells the given user good night\n\n5.choose <options>\n------------------\nInfo:The Bot chooses between the options provided(leave a space after every option)\n\n6.ask /<question>\n-----------------\nInfo: You can ask questions that will be sent to the moderators of the server(be sure to include the '/' before the question)\n\n7.eightball <question>\n--------------------\nInfo:The bot gives you its opinion on the question.\n\nMy daddy is DeltaRager```")
    
