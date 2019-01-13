import urllib.request
import json
import urllib
import discord
from discord.ext import commands

async def subcount(ctx,garith):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCGZPDIh0EIn4Rn8jdf6gSDA&key=AIzaSyC9PM7mQBumbwCFo18sBq9-NdZf5EJgDy4").read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    views = json.loads(data)["items"][0]["statistics"]["viewCount"]
    await garith.say("*We have* **"+ "{:,d}".format(int(subs)) + "** *Subscribers and* **"+"{:,d}".format(int(views))+"** *views*")
