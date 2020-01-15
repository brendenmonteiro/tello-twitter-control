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

    # def controller(command,value):
    #     if command == "takeoff":
    #         print("takeoff")
    #     elif command == "land":
    #         print("land")
    #     elif command == "up":
    #         print("up",value) 
    #     elif command == "down":
    #         print("down",value)
    #     elif command == "left":
    #         print("left",value)
    #     elif command == "right":
    #         print("right",value)
    #     elif command == "forward":
    #         print("forward",value)
    #     elif command == "back":
    #         print("back",value)
    #     elif command == "cw":
    #         print("cw",value)
    #     elif command == "ccw":
    #         print("ccw",value)
    #     elif command == "speed":
    #         print("speed",value)
    #     else:
    #         print("failure")

    def controller(command,value):
        if command == "takeoff":
            drone.takeoff()
        elif command == "land":
            drone.land()
        elif command == "up":
            drone.up(value)
        elif command == "down":
            drone.down(value)
        elif command == "left":
            drone.left(value)
        elif command == "right":
            drone.right(value)
        elif command == "forward":
            drone.forward(value)
        elif command == "back":
            drone.backward(value)
        elif command == "cw":
            drone.clockwise(value)
        elif command == "ccw":
            drone.counter_clockwise(value)
        elif command == "palmland":
            drone.palm_land()
        else:
            print("failure")


    def inputHandler(input):
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