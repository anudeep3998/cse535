#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Readme

check if u have python3 -> type python or python3

In this file :
--------------
update your values for 
    ckey
    csecret
    atoken
    asecret


'''

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import json
import requests
import sys
import subprocess
import os
import inspect
import time
from multiprocessing import process

from customTweet import customTweet

ckey = 'ZiS77nnXgwbPIVZ5AsvxERCnK'
csecret = 'VKcf7Sfd5mwmpcjSuGOWVCkiLMfpoMOZ5i4LLidCZtwhMUBv8Q'
atoken = '3526839621-Poj6uaa1CNn5WPXK3GFD91NMs0Do1WON3yxkUpE'
asecret = 'Fo0YlmTqMnLbeH3GsgNn1VyEmCIW3IGWuDKDrQ6cWWXD3'

input_file = 'input.txt'
output_conf_file = 'output.conf'
output_file_prefix = 'output_'
dirname = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def sanitize_str(string):
    string = string.replace('\n','')
    string = string.replace('\r','')
    string = string.replace('\t','')
    return string.replace('"','')


def get_terms(fname):
    term_set = []
    with open(fname) as f:
        for i, l in enumerate(f):
            term_set.append(l.split(" "))
    return i + 1, term_set

def sanitize_str_set(se):
    for s in range(len(se)):
        for t in range(len(se[s])):
            se[s][t] = sanitize_str(se[s][t])

def call_stream(ts,langs,term_set):
    ts.filter(languages=langs,track=term_set)

topic_count, term_set = get_terms(os.path.join(dirname,input_file))
sanitize_str_set(term_set)

count = 0
init_by = 'user'
current_topic = 1
total_count = 0

_INTERESTING_LIMIT_PER_TOPIC = 5
_TIME_LIMIT_PER_TOPIC_IN_MILLIS = 2000
_TOTAL_TWEET_LIMIT = 2000

headers = {'Content-type':'application/json'}
langs = ['de','ru','sp','ar','fr','ko','en']


class twitterListener(StreamListener) :
    global current_topic
    global count
    global tw_writer
    global init_by
    global total_count
    
    def __init__(self):
        super().__init__()

    def on_data(self, data) :
        global count
        global tw_writer
        global _INTERESTING_LIMIT_PER_TOPIC
        global init_by
        global output_file_prefix
        global dirname
        global current_topic
        global total_count
        
        tweet = customTweet(data)

        count += 1
        total_count += 1
        print("Topic : "+ str(current_topic)+" count ::"+str(count)+" lang : "+tweet.lang)
        if (count < _INTERESTING_LIMIT_PER_TOPIC) :
            with open(os.path.join(dirname,output_file_prefix + str(current_topic) + ".json"),"a+",encoding="utf-8") as out :
                out.write(tweet.encode_to_json()+"\n")
        else :
            count = 0
            return False

        return True
        
    def on_error(self, status) :
        print(status)
        

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

if __name__ == '__main__':
    try:
        twitterStream = Stream(auth,twitterListener())
        msg = " initiated run"
    
        try:
            if sys.argv[1] == "cron":
                msg = "cron" + msg
                init_by = 'cron'
            else:
                msg = "user" + msg
                init_by = 'user'
        except Exception:
             msg = "user" + msg
             init_by = 'user'
        print(msg)
        while total_count < _TOTAL_TWEET_LIMIT:
            for i in range(topic_count):
                current_topic = i + 1
                print("retrieving tweets for topic : "+str(current_topic) + " terms :: " + str(term_set[i]))
                #p = process.  (target=call_stream, name='call_stream', args=(twitterStream,langs,term_set[i]))
                #p.start()
                #time.sleep(2)
                #if p.is_alive():
                #    p.terminate()
                #    p.join()
                twitterStream.filter(languages=langs,track=term_set[i])

        print("Finished")
    
    except KeyboardInterrupt:
        sys.exit(0) 

