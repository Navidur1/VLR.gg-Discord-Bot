import discord
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_call(req):
    response = requests.get('https://vlrggapi.herokuapp.com/news')
    jsonData = json.loads(response.text)
    return jsonData['data']['segments'][0]['description']


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('/news'):
        msg = get_call('/news')
        await message.channel.send(msg)

    if message.content == ('/matches/results'):
        msg = get_call('/matches/results')
        await message.channel.send(msg)

client.run(os.getenv('TOKEN'))
