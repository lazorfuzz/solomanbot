# utils

## fetch_meme
```python
fetch_meme()
```
Fetches and returns buffer data for a random meme

Returns:
    Buffer -- The meme image bytes

## fetch_imdb
```python
fetch_imdb(imdb_id)
```
Fetches and returns movie metadata from IMDb

Arguments:
    imdb_id {str} -- The IMDb ID of the movie

Returns:
    str -- A string formatted for a Discord message

## rand_intro
```python
rand_intro()
```
Returns a random bot intro

Returns:
    str -- Intro message

## rand_lf_comment
```python
rand_lf_comment()
```
Returns a random leonflix compliment

Returns:
    str -- Random compliment

## has_hello
```python
has_hello(msg)
```
Check if message has a greeting

Arguments:
    msg {str} -- The message to parse

Returns:
    bool -- Whether or not a greeting was detected in the message

# tests

## TestControllers
```python
TestControllers(self, methodName='runTest')
```
Tests the bot utils methods in utils.py

### test_fetch_meme
```python
TestControllers.test_fetch_meme(self)
```
Tests that the fetched meme has a getvalue method and returns a value len > 10

### test_rand_intro
```python
TestControllers.test_rand_intro(self)
```
Tests that the intro string is not empty

### test_rand_comment
```python
TestControllers.test_rand_comment(self)
```
Tests that the comment string is not empty

# message_handlers

## greeting
```python
greeting(message)
```
Generate a greeting message

Arguments:
    message {discord.Message} -- Message

Returns:
    bool -- Whether or not the message was handled

## meme
```python
meme(message)
```
Generate a meme message

Arguments:
    message {discord.Message} -- Message

Returns:
    bool -- Whether or not the message was handled

## lf
```python
lf(message)
```
Generate a LF compliment

Arguments:
    message {discord.Message} -- Message

Returns:
    bool -- Whether or not the message was handled

