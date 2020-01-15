from datetime import time

import tweepy as tw

consumer_key = 'R0CMif2aZNAaYHxlZq1c2W9Ks'
consumer_secret = 'T0ynpdzVZxsSnCGzMoRoBjvBRzOCpj2MFb6DKSAgGiRZTGYCr4'
access_token = '1216609358513164288-NvkEo8VLra283rXQOVYGeIUam4s5SY'
access_secret = 'NX2UikUF2EcOFJ4TGtE7J2XwhGiwJlouulm2Dvtee1qc2'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

tweets = []
username = 'de_vishan'
count = 100
for tweet in api.user_timeline(id=username, count=count):
    tweets.append(tweet.text)
for tweet in tweets:
    print(tweet)
    print("...........................................................................................................")

# search_words = "#martingarrix"
# date_since = "2020-01-12"
#
# tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(100)
#
# # for tweet in tweets:
# #     print(tweet.text)
# #     print("...........................................................................................................")

#
# target = 'BrendenMonteiro'
# print("Getting data for " + target)
# item = api.get_user(target)
# print("name: " + item.name)
# print("screen_name: " + item.screen_name)
# print("description: " + item.description)
# print("statuses_count: " + str(item.statuses_count))
# print("friends_count: " + str(item.friends_count))
# print("followers_count: " + str(item.followers_count))


