import discord
import os
import requests # allows us to make an HTTP request to an API
import json # the data returned from an API will be in json
import random

TOKEN = os.environ['TOKEN']

# create an instance of a client, The way we connect to discord. 

client = discord.Client()

def get_quote():
    response = ["You can do it!", "Don't give up", "You got this!", "Believe it!"]
    randomIndex = random.randint(0, len(response)-1)
    return response[randomIndex]
"""
Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.

-- a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.
"""
# this is called when the bot is ready to be used
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# this event is triggered each time a message is recieved But if the message is from the bot we don't want it to response to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith('$hello'):
        await message.channel.send(get_quote()) 

client.run(TOKEN)