# solomanbot

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Build Status](https://travis-ci.com/lazorfuzz/solomanbot.svg?branch=master)](https://travis-ci.com/lazorfuzz/solomanbot) 

Built with asyncio. The bot currently only dispenses memes and says hi, but more functionality is planned. This is a learning project to gain familiarity with Python 3's async/await syntax and to do IO asynchronously like in Node.js.

## Getting Started
Install requirements and run the bot
```
pip3 install -r requirements.txt
python3 bot.py
```

## Running Tests
```
python3 tests.py
```

## Environment Variables
```
TOKEN='SECRET_HERE'
MEME_ENDPOINT='MEME_ENDPOINT'
APP_NAME='APP_NAME'
```

## Docs
Can be found <a href="docs.md">here</a>.

To update docs.md, install pydocmd and run the gendocs script
```
pip3 install pydoc-markdown
./gendocs
```

## Python Version

The minimum Python version required for this bot is 3.6.
