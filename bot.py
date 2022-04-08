import discord
import requests
import json

def get_call(req):
    response = requests.get('https://vlrggapi.herokuapp.com/news')
    json_data = json.loads(response.text)
    return json_data['data']['segments'][0]['description']

client = discord.Client()

discord.utils.oauth_url('OTYxODQxMTI1MjczMDA2MDgw.Yk-2Wg.EpHng1F2RyA2on2uDhEx_G3XTEo')

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

client.run('OTYxODQxMTI1MjczMDA2MDgw.Yk-2Wg.EpHng1F2RyA2on2uDhEx_G3XTEo')
