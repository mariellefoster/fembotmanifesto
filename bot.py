# @authors Marf and May Waver
# May 2017

import markovify
import tweepy
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

# Get raw text as string.
with open("manifestos.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

common_sentences = ["By the late twentieth century.",]

# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(10):
#     print(text_model.make_short_sentence(140))

tweet = text_model.make_short_sentence(140)
while tweet in common_sentences:
    tweet = text_model.make_short_sentence(140)

api.update_status(tweet)

