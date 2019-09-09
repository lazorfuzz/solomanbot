import aiohttp
from io import BytesIO
from bs4 import BeautifulSoup
import random


async def fetch_meme(message):
  url = 'https://leonflix.pythonanywhere.com/memes/random'
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      meme_data = await resp.json()
      meme_url = meme_data['url']
      print('Sending meme:', meme_data['id'])
    async with session.get(meme_url) as resp:
      buffer = BytesIO(await resp.read())
  return buffer

async def fetch_imdb(imdb_id):
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
  intros = ['*pops out of a trash can*', '*walks out behind a car*', '*sets down silver play button*', '*calls in from florida penitentiary*', '*turns off lawn mower*', '*snorts giant line of PCP*']
  return random.choice(intros)

def rand_leonflix_comment():
  comments = ['This app may be the Kodi killer', 'Sorry Kodi, I\'m using this instead', 'Kodi\'s competition is finally here', 'Who needs Exodus when you have Leonflix', 'This app will revolutionize streaming']
  return random.choice(comments)

def has_hello(msg):
  hellos = ['hi ', 'hello ', 'good morning ', 'hey ']
  there = list(filter(lambda h: msg.lower().startswith(h), hellos))
  return len(there) > 0
