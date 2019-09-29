import utils
import discord


client = None

async def greeting(message):
  if '<@%s' % client.user.id in message.content and utils.has_hello(message.content):
    msg = 'Hello %s!' % (message.author)
    await message.channel.send(msg)
    return True
  return False

async def meme(message):
  if message.content == '!meme':
    buffer = await utils.fetch_meme()
    await message.channel.send(content="Hello I hope everybody is doing great", file=discord.File(fp=buffer, filename='meme.png'))
    return True
  return False

async def leonflix(message):
  if 'leonflix' in message.content.lower():
    await message.channel.send('%s\n%s' % (utils.rand_intro(), utils.rand_leonflix_comment()))
    return True
  return False

parsers = [greeting, meme, leonflix]
