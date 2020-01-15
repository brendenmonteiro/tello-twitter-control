from datetime import time

import tweepy as tw
import credentials as cred
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print ("error")
        print (status)

auth = OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#hwu2020tello"])


# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
# api = tw.API(auth)

# tweets = []
# username = 'raptorisonline'
# count = 100
# for tweet in api.user_timeline(id=username, count=count):
#     tweets.append(tweet.text)
# for tweet in tweets:
#     print(tweet)
#     print("...........................................................................................................")

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


