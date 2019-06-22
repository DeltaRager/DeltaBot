import discord
from discord.ext import commands
import json


async def text(ctx):
        data = {}
        data['people'] = []
        data['people'].append({
                'name': 'hello',
                'website': 'stackabuse.com',
                'from': 'Nebraska'
                })
        data['people'].append({
                'name': 'Larry',
                'website': 'google.com',
                'from': 'Michigan'
                })
        data['people'].append({
                'name': 'Tim',
                'website': 'apple.com',
                'from': 'Alabama'
                })
        with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
