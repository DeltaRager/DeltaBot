import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands


async def choose(garith,message):
    await garith.send_message(message.channel,"**Ze Commands** \n```Prefix: 'g!' \n\nHelp\n----\nInfo:Give you the juicy commands```")
    
