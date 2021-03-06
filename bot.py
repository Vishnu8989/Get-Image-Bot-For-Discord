from datetime import datetime
from typing import Generator
import discord
import config
import generator as gen


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
        quote = gen.get_quote()
        await message.channel.send(quote)
        picture = "quote"
        await message.channel.send("Wait that's not all ,\nHere is a random \"Quote\" pic...")
        gen.get_pic(picture)
        date_time = config.date_time
        image_name = './'+picture+'_' + date_time + '.jpg'
        await message.channel.send(file=discord.File(image_name))

    if message.content.startswith('$pic'):
        picture = msg.split("$pic ", 1)[1]
        await message.channel.send("Loading a random {} picture...".format(picture))
        gen.get_pic(picture)
        date_time = config.date_time
        # print("Bot : "+date_time)
        image_name = './'+picture+'_' + date_time + '.jpg'
        # print("Image : "+image_name)
        await message.channel.send("\n\n\nAnd here it is ")
        await message.channel.send(file=discord.File(image_name))


client.run(config.key)
# https://discord.com/api/oauth2/authorize?client_id=910505990850506793&permissions=534723947584&scope=bot
# to run this bot you will need a key so please contact me for demo!!!!!!
