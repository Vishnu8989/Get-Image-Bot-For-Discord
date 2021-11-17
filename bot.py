import discord
import os
import requests  # allow code to make http requests
import json  # to help in returned json files from http requests
import random
from replit import db
import shutil
import config


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def get_pic(name):
    image_url = "https://source.unsplash.com/800x450/?{}".format(name)
    # print(image_url)
    response = requests.get(image_url, stream=True)
    file = open("test1.jpg", "wb")
    response.raw_decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response



client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# respond to hello
@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        get_pic("motivational")
        await message.channel.send(file=discord.File('./test1.jpg'))


    if message.content.startswith('$pic'):
        picture = msg.split("$pic ", 1)[1]
        get_pic(picture)
        await message.channel.send("Wait Good Things take time")
        await message.channel.send(file=discord.File('./test1.jpg'))


client.run(config.key);
