#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @authors Marf and May Waver
# May 2017

import markovify
import tweepy
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

# Get raw text as string.
with open("manifestos-lower.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

common_sentences = ["By the late twentieth century.", 
                    "another important thing in life.",
                    "we take our land.",
                    "we are survivors who are certain deadweight.",
                    "in my career. i'd rather make my social interactions profitable to me.",
                    "<<officer carrie johnson, who had heard debris fall from the outset, expressly to preclude victims from ever exiting a violent situation.",
                    "this chapter is an optical illusion."]

# # # Print three randomly-generated sentences of no more than 140 characters
# for i in range(10):
#     print(text_model.make_short_sentence(140))

tweet = text_model.make_short_sentence(140)
while tweet in common_sentences or tweet is None:
    tweet = text_model.make_short_sentence(140)

api.update_status(tweet)

