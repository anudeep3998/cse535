
import json
import urllib


class customTweet :
    
    _id = '0'               #user_id of the tweeter
    lang = 'en'             #language of the tweeet
    created_at = ''         #UTC time when the tweet was posted
    coordinates = [-1,-1]   #[longitude,latitude]
    text = ''               #text of tweeet
    
    lang_set_en = ['en','en-us','en-gb','en-au','en-ca','en-nz','en-ie','en-za','en-jm','en-bz','en-tt','en-in']
    lang_set_de = ['de','de-ch','de-at','de-li','de-lu']
    lang_set_ru = ['ru','ru-mo']
    
    term_set = ['health','Gesundheit','здоровье', 'самочувствие','здравие','cancer','disease', \
                'blood','AIDS','Krebs','Krebsgeschwür', 'Krankheit', 'Erkrankung', \
                'болезнь','заболевание','недуг','карцинома']

    
    def __init__(self, text):
    
        try:
            json_text = json.loads(text)
            self._id = json_text['id_str']
        except KeyError:
            pass
        
        try:
            self.lang = json_text['lang']
        except KeyError:
            pass
        
        try:
            self.created_at = json_text['created_at']
        except KeyError:
            pass
        
        try:
            self.coordinates = json_text['coordinates']['coordinates']
            if not self.coordinates:
                self.coordinates = [-1,-1]
        except KeyError:
            self.coordinates = [-1,-1]
        except TypeError:
            self.coordinates = [-1,-1]
        
        try:
            self.text = json_text['text']
        except KeyError:
            pass


    def set_vals(self, _id='0',lang='en',created_at='',coordinates=[-1,-1],text=''):
        self._id = _id
        self.lang = lang
        self.created_at = created_at
        self.coordinates = coordinates
        self.text = text

    def is_lang_english (self):
        #global lang_set_en
        #return self.lang in self.lang_set_en
        return False
        
    def is_lang_german (self):
        #global lang_set_de
        return self.lang in self.lang_set_de
  
    def is_lang_russian (self):
        #global lang_set_ru
        return self.lang in self.lang_set_ru
    
    def is_lang_interesting (self):
        return self.is_lang_english() or self.is_lang_german() or self.is_lang_russian()
    
    
    def is_term_interesting (self):
        for term in self.term_set:
            for word in self.text.split():
                if word.lower() == term.lower():     #direct comparision works for German, English and Russian. Problems only seem to be with Greek and Turkish
                    return True
        return False
    
    def encode_to_json (self):
        str_tweet = '[{'
        str_tweet += ' "id" : "'+ self._id + '",'
        str_tweet += ' "lang" : "'+ self.lang + '",'
        str_tweet += ' "created_at" : "'+ self.created_at + '",'
        str_tweet += ' "coordinates" : { "longitude" : '+ str(self.coordinates[0]) + ', "latitude" :' + str(self.coordinates[1]) + '},'
        str_tweet += ' "text" : "'+ urllib.parse.quote_plus(self.text) + '"'
        str_tweet += '}]'
        
        #print(json.loads(str_tweet))
        return str_tweet
