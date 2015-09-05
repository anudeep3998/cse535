from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import json
import requests
import sys
from customTweet import customTweet

ckey = 'ZiS77nnXgwbPIVZ5AsvxERCnK'
csecret = 'VKcf7Sfd5mwmpcjSuGOWVCkiLMfpoMOZ5i4LLidCZtwhMUBv8Q'
atoken = '3526839621-Poj6uaa1CNn5WPXK3GFD91NMs0Do1WON3yxkUpE'
asecret = 'Fo0YlmTqMnLbeH3GsgNn1VyEmCIW3IGWuDKDrQ6cWWXD3'

count = 1
interesting_count=1
int_german=0
int_russian=0

update_url = ['http://localhost:8983/solr/gettingstarted/update/json/docs','http://localhost:7574/solr/gettingstarted/update/json/docs']
update_url_args = ['?split=/'+ \
                  '&f=id:/id' + \
                  '&f=lang:/lang' + \
                  '&f=created_at:/created_at' + \
                  '&f=longitude:/coordinates/longitude' + \
                  '&f=latitude:/coordinates/latitude' + \
                  '&f=text:/text'+ \
                  '&commit=true'+ \
                  '&data=' , \
                  \
                  '?split=/'+ \
                  '&f=id:/id' + \
                  '&f=lang:/lang' + \
                  '&f=created_at:/created_at' + \
                  '&f=longitude:/coordinates/longitude' + \
                  '&f=latitude:/coordinates/latitude' + \
                  '&f=text:/text'+ \
                  '&data='
                  ]

headers = {'Content-type':'application/json'}


class twitterListener(StreamListener) :

    def on_data(self, data) :
        global count
        global interesting_count
        global int_german
        global int_russian
        tweet = customTweet(data)
        
        if tweet.is_lang_interesting() and tweet.is_term_interesting():
            if tweet.is_lang_german():
                int_german = int_german + 1
            if tweet.is_lang_russian():
                int_russian = int_russian + 1
            print("Got a new tweet :: Total # : "+ str(int_german)+"-"+str(int_russian)+"|"+str(interesting_count-int_german-int_russian)+"/"+str(count))
            interesting_count+=1
            if interesting_count <= 50:
                req = requests.post(update_url[count%2]+update_url_args[0 if count%25==0 else 1], data = tweet.encode_to_json(), headers=headers)
                #print(req.text)
                #print("Pushing to SOLR : return# "+str(req.status_code))
            else:
                '''
                    commit both cores. One duplicate tweet will be added to one of the core, but shouldn't matter over the other count
                '''
                req = requests.post(update_url[1]+update_url_args[0], data = tweet.encode_to_json(), headers=headers)
                req = requests.post(update_url[0]+update_url_args[0], data = tweet.encode_to_json(), headers=headers)
                sys.exit(0)
        else:
            print("Unkown or uninteresting language/term, skipping. Scanned["+str(count)+"]")
        #print("Got a new tweet :: "+parsed_text['text'].encode('ascii', 'ignore').decode('ascii')+"\nTotal # : "+ str(count))
        count = count + 1
        return True
        
    def on_error(self, status) :
        print(status)
        

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,twitterListener())
twitterStream.filter(track=['health'])
