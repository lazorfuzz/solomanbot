import utils
import discord
import os


client = None
APP_NAME = os.getenv('APP_NAME')

async def greeting(message):
  """Generate a greeting message
  
  Arguments:
      message {discord.Message} -- Message
  
  Returns:
      bool -- Whether or not the message was handled
  """
  if '<@%s' % client.user.id in message.content and utils.has_hello(message.content):
    msg = 'Hello %s!' % (message.author)
    await message.channel.send(msg)
    return True
  return False

async def meme(message):
  """Generate a meme message
  
  Arguments:
      message {discord.Message} -- Message
  
  Returns:
      bool -- Whether or not the message was handled
  """
  if message.content == '!meme':
    buffer = await utils.fetch_meme()
    await message.channel.send(content="Hello I hope everybody is doing great", file=discord.File(fp=buffer, filename='meme.png'))
    return True
  return False

async def lf(message):
  """Generate a LF compliment
  
  Arguments:
      message {discord.Message} -- Message
  
  Returns:
      bool -- Whether or not the message was handled
  """
  if APP_NAME.lower() in message.content.lower():
    await message.channel.send('%s\n%s' % (utils.rand_intro(), utils.rand_lf_comment()))
    return True
  return False

parsers = [greeting, meme, lf]
