# importing our packages
import discord
import random
import time
import asyncio
import datetime
from datetime import date
import calendar

# tryna connect our bot to the server...client = discord.client(our bot)
TOKEN = "NzMzODU2NjYyMzYzOTYzNDMy.XxJPRg.-6OB8rPA0ED-6URRSPgLW1B9CQY"

client = discord.Client()
channel = client.get_channel(851169143767302154)

# SHIT
day = datetime.date.today()
print(day)


@client.event
async def on_ready():
    await channel.send("I'm here.")


@client.event
async def on_disconnect():
    await channel.send("LOl I'm leaving")


@client.loop(hours=24)
async def good_morning():
    await channel.send("Rise and Shine you 'lil assolotls!")


@client.event
async def hi_message(raw_message):
    message = raw_message.lower().content
    if message == 'yada hi':
        await channel.send('Hello assolotls!')
    if message.author == client.user:
        return

    if message.startswith('yada'):
        quote = "aksdjbsakjd"
        await message.channel.send(quote)

# run bot on discord server authorizing stuffs(https://discordapi.com/permissions.html)
client.run(TOKEN)

# this bot can turn a message into it's skyline, figlet, all caps, and all lower version
# it can send a good morning and good night message
# it can take a message, and search on youtube, and pick the first video, and play it (if no message input, send this: https://www.youtube.com/watch?v=7NuaK29J1fM)
# it can take a message, and search on google images, and pick the first image and send it (if no message input, send this: https://media1.giphy.com/media/l2JhpjWPccQhsAMfu/200.gif)
# it can take your message word, and return a list of synonyms and antonyms
