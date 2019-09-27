import discord
import re
import secrets
import utils
import message_handlers


client = discord.Client()
message_handlers.client = client
parsers = message_handlers.parsers

@client.event
async def on_message(message):
  """Async event handler for receiving messages
  """
  if message.author == client.user:
    return
  print(message.content)
  for parse_message in parsers:
    status = await parse_message(message)
    if status:
      break

@client.event
async def on_ready():
  """Async event handler for when the client is logged in
  """
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

client.run(secrets.TOKEN)