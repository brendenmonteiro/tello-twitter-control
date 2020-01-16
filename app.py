from datetime import time

import json

import tweepy as tw
import credentials as cred
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from time import sleep
import tellopy

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)
# drone = tellopy.Tello()
try:
    # drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
    # drone.connect()
    # drone.wait_for_connection(60.0)

    def controller(command,value):
        if command == "takeoff":
            drone.takeoff()
            print("takeoff")
        elif command == "land":
            drone.land()
            print("land")
        elif command == "up":
            drone.up(value)
            print("up",value)
        elif command == "down":
            drone.down(value)
            print("down",value)
        elif command == "left":
            drone.left(value)
            print("left",value)
        elif command == "right":
            drone.right(value)
            print("right",value)
        elif command == "forward":
            drone.forward(value)
            print("forward",value)
        elif command == "back":
            drone.backward(value)
            print("back",value)
        elif command == "cw":
            drone.clockwise(value)
            print("cw",value)
        elif command == "ccw":
            drone.counter_clockwise(value)
            print("ccw",value)
        elif command == "palmland":
            drone.palm_land()
            print("palm_land")
        else:
            print("failure")


    def inputHandler(input):
        input = input.rstrip()
        input = input.lower()
        command=input
        value=0
        controller(command,value)

    class listener(StreamListener):

        def on_data(self, data):
            tweetjson=json.loads(data)
            inputHandler(tweetjson["text"])
            return(True)

        def on_error(self, status):
            print ("error")
            print (status)

    auth = OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
    auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_SECRET)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(follow=["4888927145"])

except Exception as ex:
    print(ex)
finally:
    drone.quit()