import discord
import logging

# For logging to file
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

logging.basicConfig()

client = discord.Client()

#discord.utils.oauth_url('OTYxODQxMTI1MjczMDA2MDgw.Yk-2Wg.Y8sOYTb7cFdZIhND2GIsVieag-8')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('$hello'):
        await message.channel.send('Hello!')

client.run('OTYxODQxMTI1MjczMDA2MDgw.Yk-2Wg.Y8sOYTb7cFdZIhND2GIsVieag-8')
