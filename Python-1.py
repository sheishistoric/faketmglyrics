#!/usr/bin/env python
import os
from markovbot import Markovbot
#Initialize a MarkovBot instance
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath(a/a))
# Construct the path to the book
book = os.path.join(dirname, 'tmg copy.text')
# Make your bot read the book!
tweetbot.read(book)
my_first_text = tweetbot.generate_text(25, seedword=['you', 'I am'])
print("tweetbot says:")
print(my_first_text)
# Consumer Key (API Key)
cons_key = 'a'
# Consumer Secret (API Secret)
cons_secret = 'a'
# Access Token
access_token = 'a'
# Access Token Secret
access_token_secret = 'a'
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
