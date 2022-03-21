import discord
import os
TOKEN = os.environ['TOKEN']

# create an instance of a client, The way we connect to discord. 

client = discord.Client()

# this is called when the bot is ready to be used

"""
Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.

-- a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.
"""
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# this event is triggered each time a message is recieved But if the message is from the bot we don't want it to response to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!') 

client.run(TOKEN)