import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from PIL import Image
from io import BytesIO
import discord
from discord.ext import commands
import asyncio


async def fortniteleader(ctx,garith):
    tmp = await garith.say("**Loading current leaderboard...**")

    driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')  
    driver.get('https://fortnitetracker.com/leaderboards')
    driver.maximize_window()

    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="leaderboard"]/section/div/div[5]/table/tbody/tr[1]') 
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()


    im = Image.open(BytesIO(png)) 

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) 
    im.save('leaderboard1.png')

    element = driver.find_element_by_xpath('//*[@id="leaderboard"]/section/div/div[5]/table/tbody/tr[2]') 
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()


    im = Image.open(BytesIO(png)) 

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) 
    im.save('leaderboard2.png')

    element = driver.find_element_by_xpath('//*[@id="leaderboard"]/section/div/div[5]/table/tbody/tr[3]') 
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()
    driver.quit()


    im = Image.open(BytesIO(png)) 

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) 
    im.save('leaderboard3.png')


    await garith.edit_message(tmp , '**The Fortnite Leaderboard**')
    with open(r'E:\ForBot\DeltaBot\leaderboard1.png', 'rb') as picture1, open(r'C:\Users\Abi\Desktop\Bot #2\leaderboard2.png', 'rb') as picture2, open(r'C:\Users\Abi\Desktop\Bot #2\leaderboard3.png', 'rb') as picture3:
        await garith.send_file(ctx.message.channel, picture1)
        await garith.send_file(ctx.message.channel, picture2)
        await garith.send_file(ctx.message.channel, picture3)

