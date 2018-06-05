#!/usr/bin/env python
import os
import time
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from markovbot import MarkovBot
#Initialize a MarkovBot instance
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath("tmg copy.text"))
# Construct the path to the book
book = os.path.join(dirname, 'tmg copy.text')
# Make your bot read the book!
tweetbot.read(book)
my_first_text = tweetbot.generate_text(25, seedword=['you', 'I am', 'going to', 'my', 'love',])
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
# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=6, minutes=30, keywords=None, prefix=None, suffix=None)
secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)
