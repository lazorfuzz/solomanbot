import aiohttp
from io import BytesIO
import os
from bs4 import BeautifulSoup
import random


async def fetch_meme():
  """Fetches and returns buffer data for a random meme
  
  Returns:
      Buffer -- The meme image bytes
  """
  url = os.getenv('MEME_ENDPOINT')
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      meme_data = await resp.json()
      print('Sending meme:', meme_data['id'])
    async with session.get(meme_data['url']) as resp:
      buffer = BytesIO(await resp.read())
  return buffer

async def fetch_imdb(imdb_id):
  """Fetches and returns movie metadata from IMDb
  
  Arguments:
      imdb_id {str} -- The IMDb ID of the movie
  
  Returns:
      str -- A string formatted for a Discord message
  """
  url = 'https://www.imdb.com/title/%s' % imdb_id
  print(url)
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as res:
      data = await res.text()
      print(data)
      soup = BeautifulSoup(data)
      print(soup.find('h1'))
      return soup.find('h1')

def rand_intro():
  """Returns a random bot intro
  
  Returns:
      str -- Intro message
  """
  intros = ['*pops out of a trash can*', '*walks out behind a car*', '*sets down silver play button*', '*calls in from florida penitentiary*', '*turns off lawn mower*', '*dabs*', '*sits behind table*']
  return random.choice(intros)

def rand_lf_comment():
  """Returns a random leonflix compliment
  
  Returns:
      str -- Random compliment
  """
  comments = ['This app may be the Kodi killer', 'Sorry Kodi, I\'m using this instead', 'Kodi\'s competition is finally here', 'Who needs Exodus when you have %s' % os.getenv('APP_NAME'), 'This app will revolutionize streaming']
  return random.choice(comments)

def has_hello(msg):
  """Check if message has a greeting
  
  Arguments:
      msg {str} -- The message to parse
  
  Returns:
      bool -- Whether or not a greeting was detected in the message
  """
  hellos = ['hi ', 'hello ', 'good morning ', 'hey ', 'sup ']
  there = list(filter(lambda h: msg.lower().startswith(h), hellos))
  return len(there) > 0
