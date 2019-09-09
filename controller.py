import aiohttp
from io import BytesIO
from bs4 import BeautifulSoup


async def fetch_meme(message):
  url = 'https://leonflix.pythonanywhere.com/memes/random'
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      meme_data = await resp.json()
      meme_url = meme_data['url']
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

