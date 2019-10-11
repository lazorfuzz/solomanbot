# solomanbot

Soloman: The Discord bot.

Built in Python with asyncio. The bot currently only dispenses memes and says hi, but more functionality is planned. This is a learning project to gain familiarity with Python 3's async/await syntax and to do IO asynchronously like in Node.js.

## Getting Started
Add your bot's client secret to `_secrets.py` and rename the file to `secrets.py`

Then, install requirements and run the bot
```
pip3 install -r requirements.txt
python3 bot.py
```

## Running Tests
```
python3 tests.py
```

## Docs
Can be found <a href="docs.md">here</a>.

To update docs.md, install pydocmd and run the gendocs script
```
pip install pydoc-markdown
./gendocs
```

## Python Version

The minimum Python version required for this bot is 3.6.
