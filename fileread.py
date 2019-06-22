import discord
from discord.ext import commands
import json


async def text(ctx):
        data='it works'
        with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
