import discord
import os
import requests # allows us to make an HTTP request to an API
import json # the data returned from an API will be in json
import random
from replit import db
from keep_alive import keep_alive


TOKEN = os.environ['TOKEN']

# create an instance of a client, The way we connect to discord. 

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "upset", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there",
    "You are a great person"
    ]

if "responding" not in db.keys():
    db["responding"] = True

def get_quote():
    response = ["You can do it!", "Don't give up", "You got this!", "Believe it!"]
    randomIndex = random.randint(0, len(response)-1)
    return response[randomIndex]

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

"""
Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.

-- a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.
"""
# this is called when the bot is ready to be used
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

aList = ["apple", "banana"]
# this event is triggered each time a message is recieved But if the message is from the bot we don't want it to response to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content
    
    if msg.startswith('$hello'):
        await message.channel.send(get_quote()) 
    if db["responding"]:
        options = starter_encouragements
        for k, v in db.items():
            print("keys: ", k)
            print("values: ", v)
        if "encouragements" in db.keys():
            options.extend(db["encouragements"])
    
    
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db.get_raw("encouragements")
        await message.channel.send(encouragements)
            
    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements.extend(db["encouragements"])
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

keep_alive()
client.run(TOKEN)