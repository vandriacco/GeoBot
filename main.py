import discord
import os
import requests
import re

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if (message.author == client.user):
        return

    if (message.content.startswith('!!ping!')):
      await message.channel.send('pong!')
      
    convert_str = '-convert'
    if (message.content.startswith(convert_str)):
      command = message.content[len(convert_str)+1:]
      tokens = command.split(' ')
      
      parameters = {
        "from": tokens[0],
        "to": tokens[2],
        "amount": float(tokens[4])
      }

      url = 'https://api.exchangerate.host/convert?from={}&to={}'
      response = requests.get(url.format(parameters["from"], parameters["to"]))
      data = response.json()
      await message.channel.send(data['result'] * parameters["amount"])


client.run(os.getenv('TOKEN'))
