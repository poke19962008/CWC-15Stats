__author__ = 'poke19962008'

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import re

class StdOutListener(StreamListener):

    def on_data(self, data):
        json_data = json.loads(str(data))

        ID = str(json_data['id'])
        place = str(json_data['place'])
        usr_location = json_data['user']['location'].encode('utf-8')

        if (re.search("India", usr_location)) or (re.search("India", place)):
            location =  "{ID: "+ ID + ", Place: " + place + ", User Location: " + usr_location + "}"
            print(location)

            tweet_loc_file.write(location + "\n")
            tweet_file.write(str(json_data) + "\n")

        return True


    def on_error(self, status):
        print status

if __name__ == '__main__':

    tweet_file = open("tweet_stream.txt", "a")
    tweet_loc_file = open("tweet_location.txt", "a")

    con_key = ""
    con_sec = ""
    acc_tok = ""
    acc_sec = ""

    auth = tweepy.OAuthHandler(con_key, con_sec)
    auth.set_access_token(acc_tok, acc_sec)
    api = tweepy.API(auth)

    while True:    #9.22 3.03h
        try:
            obj = StdOutListener()
            stream = Stream(auth, obj)
            stream.filter(track=["#CWC15", "#CWC15Final", "AUSvsNZ", "NZvsAUS", "AUSvNZ", "NZvAUS"])
        except:
            continue