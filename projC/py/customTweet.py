import json
from urllib import parse
from dateutil import parser


class customTweet :
    
    _id = '0'               #id of the tweet
    lang = 'en'             #language of the tweeet
    created_at = ''         #UTC time when the tweet was posted
    coordinates = [-1,-1]   #[longitude,latitude]
    text = ''               #text of tweeet
    retweet_status = False
    quote_status = False
    user_lang = 'en'
    
    place_id = ''           #place.id
    place_type = ''         #place.place_type
    place_full_name = ''    #place.place_full_name
    place_country_code = '' #plce.country_code
    place_country = ''      #place.country
    
    hashtags = []           #entities.hashtags[].text
    trends = []             #entities.trends[].text
    urls = []               #entities.urls[].url
    expanded_urls = []      #entities.urls[].expanded_url
    symbols = []            #entites.symbols[].text
    
    timestamp = 0           #timestamp_ms

    favorite_count = 0
    retweet_count = 0
    favorited_status = False
    user_id = 0
    user_verified = False
    user_followers_count = 0
    user_screen_name = ''
    user_name = ''


    
    json_text = {}

    
    def __init__(self, text):
    
        try:
            json_text = json.loads(text, encoding="utf-8")
            self._id = json_text['id_str']
        except KeyError:
            pass
        
        try:
            self.lang = json_text['lang']
        except KeyError:
            pass

        try:
            self.favorite_count = json_text['favorite_count']
        except KeyError:
            pass

        try:
            self.retweet_count = json_text['retweet_count']
        except KeyError:
            pass

        try:
            self.favorited_status = json_text['favorited']
        except KeyError:
            self.favorited_status = False

        try:
            self.user_id = json_text['user']['id_str']
        except KeyError:
            pass

        try:
            self.user_verified = json_text['user']['verified']
        except KeyError:
            self.user_verified = False

        try:
            self.user_followers_count = json_text['user']['followers_count']
        except KeyError:
            self.user_followers_count = False

        try:
            self.user_screen_name = json_text['user']['screen_name']
        except KeyError:
            pass

        try:
            self.user_name = json_text['user']['name']
        except KeyError:
            pass

        try:
            self.user_followers_count = json_text['user']['followers_count']
        except KeyError:
            self.user_verified = False
        
        try:
            self.user_lang = json_text['user']['lang']
        except KeyError:
            pass
        
        try:
            d = json_text['created_at']
            #input       Wed Dec 09 01:49:57 +0000 2015
            #output      yyyy-MM-dd'T'HH:mm:ss'Z'
            dx = parser.parse(d)
            self.created_at = dx.strftime("%Y-%m-%dT%H:%M:%SZ")
        except KeyError:
            pass
        
        try:
            if (json_text['coordinates']) and ((json_text['coordinates']['coordinates'])) :
                self.coordinates = json_text['coordinates']['coordinates']
            else:
                self.coordinates = [-1,-1]
        except KeyError:
            self.coordinates = [-1,-1]
        except TypeError:
            self.coordinates = [-1,-1]
        
        try:
            self.text = json_text['text']
        except KeyError:
            pass
        
        try:
            if not json_text['retweeted_status']:
                self.retweet_status = False
            else :
                self.retweet_status = True
        except KeyError:
            pass
        
        try:
            if not json_text['quoted_status']:
                self.quote_status = False
            else :
                self.quote_status = True
        except KeyError:
            pass
        
        
        try:
            if not json_text['place']:
                self.place_id = ''
                self.place_type = ''
                self.place_full_name = ''
                self.place_country = ''
                self.place_country_code = ''
            else:
                try:
                    self.place_id = json_text['place']['id']
                    self.place_type = json_text['place']['place_type']
                    self.place_full_name = json_text['place']['full_name']
                    self.place_country_code = json_text['place']['country_code']
                    self.place_country = json_text['place']['country']
                    #print(json_text['place'])
                except KeyError:
                    pass
        except KeyError:
            self.place_id = ''
            self.place_type = ''
            self.place_full_name = ''
            self.place_country = ''
            self.place_country_code = ''
        
        try:
            self.hashtags = []
            self.trends = []
            self.symbols = []
            self.urls = []
            self.expanded_urls = []
            if json_text['entities'] :
                try:
                    if not json_text['entities']['hashtags'] :
                        self.hashtags = []
                    else:
                        for h in json_text['entities']['hashtags']:
                            self.hashtags.append(h['text'])
                except KeyError:
                    self.hashtags = []
                    
                try:
                    if not json_text['entities']['trends'] :
                        self.trends = []
                    else:
                        for t in json_text['entities']['trends']:
                            self.trends.append(t['text'])
                except KeyError:
                    self.trends = []
                    
                try:
                    if not json_text['entities']['symbols'] :
                        self.symbols = []
                    else:
                        for s in json_text['entities']['symbols']:
                            self.symbols.append(s['text'])
                except KeyError:
                    self.symbols = []
                    
                try:
                    if not json_text['entities']['urls'] :
                        self.urls = []
                        self.expanded_urls = []
                    else:
                        for u in json_text['entities']['urls']:
                            self.urls.append(parse.quote_plus(u['url']))
                            self.expanded_urls.append(parse.quote_plus(u['expanded_url']))
                except KeyError:
                        self.urls = []
                        self.expanded_urls = []
        except KeyError:
            self.hashtags = []
            self.trends = []
            self.symbols = []
            self.urls = []
            self.expanded_urls = []
        

    def sanitize_str(self,string):
        string = string.replace('\n','')
        string = string.replace('\r','')
        string = string.replace('\t','')
        return string.replace('"','')
 
    #currently not in use. Add other variables to complete and use
    def set_vals(self, _id='0',lang='en',created_at='',coordinates=[-1,-1],text='',retweet_status=False,quote_status=False, user_lang='en'):
        self._id = _id
        self.lang = lang
        self.created_at = created_at
        self.coordinates = coordinates
        self.text = text
        self.retweet_status = retweet_status
        self.quote_status = quote_status
        self.user_lang = user_lang
    
    
    def is_term_interesting (self):
        for term in self.term_set:
            for word in self.text.split():
                if word.lower() == term.lower():     #direct comparision works for German, English and Russian. Problems only seem to be with Greek and Turkish
                    return True
        return False

    def encode_to_json (self):
        str_tweet = '{'
        str_tweet += ' "id" : "'+ self._id + '",'
        str_tweet += ' "lang" : "'+ self.lang + '",'
        str_tweet += ' "created_at" : "'+ self.created_at + '",'
        str_tweet += ' "coordinates" : ['+ str(self.coordinates[0]) + ', ' + str(self.coordinates[1]) + '],'
        str_tweet += ' "text" : "'+ self.sanitize_str(self.text) + '",'
        str_tweet += ' "place_id" : "'+ self.place_id + '",'
        str_tweet += ' "place_type" : "'+ self.place_type + '",'
        str_tweet += ' "place_full_name" : "'+ self.place_full_name + '",'
        str_tweet += ' "place_country_code" : "'+ self.place_country_code + '",'
        str_tweet += ' "place_country" : "'+ self.place_country + '",'
        str_tweet += ' "tweet_hashtags" : "'+ str(self.hashtags) + '",'
        str_tweet += ' "trends" : "'+ str(self.trends) + '",'
        str_tweet += ' "symbols" : "'+ str(self.symbols) + '",'
        str_tweet += ' "tweet_urls" : "'+ str(self.urls) + '",'
        str_tweet += ' "expanded_urls" : "'+ str(self.expanded_urls) + '",'
        str_tweet += ' "timestamp" : "'+ str(self.timestamp) + '",'
        str_tweet += ' "retweet_status" : "'+ str(self.retweet_status) + '",'
        str_tweet += ' "retweet_count" : "'+ str(self.retweet_count) + '",'
        str_tweet += ' "quote_status" : "'+ str(self.quote_status) + '",'
        str_tweet += ' "favorite_count" : "'+ str(self.favorite_count) + '",'
        str_tweet += ' "favorited_status" : "'+ str(self.favorited_status) + '",'
        str_tweet += ' "user_id" : "'+ self.sanitize_str(self.user_id) + '",'
        str_tweet += ' "user_verified" : "'+ str(self.user_verified) + '",'
        str_tweet += ' "user_followers_count" : "'+ str(self.user_followers_count) + '",'
        str_tweet += ' "user_screen_name" : "'+ self.sanitize_str(self.user_screen_name) + '",'
        str_tweet += ' "user_name" : "'+ self.sanitize_str(self.user_name) + '",'

        if (self.lang == 'ar'):
            str_tweet += ' "text_ar" : "'+ self.sanitize_str(self.text) + '"'

        if (self.lang == 'ko'):
            str_tweet += ' "text_ko" : "'+ self.sanitize_str(self.text) + '"'

        if (self.lang == 'en'):
            str_tweet += ' "text_en" : "'+ self.sanitize_str(self.text) + '"'

        if (self.lang == 'ru'):
            str_tweet += ' "text_ru" : "'+ self.sanitize_str(self.text) + '"'

        if (self.lang == 'fr'):
            str_tweet += ' "text_fr" : "'+ self.sanitize_str(self.text) + '"'

        if (self.lang == 'sp'):
            str_tweet += ' "text_sp" : "'+ self.sanitize_str(self.text) + '"'


        str_tweet += '}'
        return str_tweet
