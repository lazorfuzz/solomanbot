import discord
import re
import secrets
import controller

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(message.content)
  # imdb_match = re.search('^tt(.{6})', message.content)
  if '<@%s' % client.user.id in message.content and controller.has_hello(message.content):
    msg = 'Hello {.author}!'.format(message)
    await message.channel.send(msg)
  elif '!meme' in message.content:
    buffer = await controller.fetch_meme()
    await message.channel.send(content="Hello I hope everybody is doing great", file=discord.File(fp=buffer, filename='meme.png'))
  elif 'leonflix' in message.content.lower():
    await message.channel.send('%s\n%s' % (controller.rand_intro(), controller.rand_leonflix_comment()))
  '''elif imdb_match:
    info = await controller.fetch_imdb(imdb_match.group())
    await message.channel.send(info)'''
    

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

client.run(secrets.TOKEN)