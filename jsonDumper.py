from fileWriter import fileWriter
from customTweet import customTweet

_static_path = "/home/anudeep3998/cse535/code/"
from_file_path = [_static_path+'tweetDump/eng2.txt', _static_path+'tweetDump/ger2.txt', _static_path+'tweetDump/rus2.txt']
to_file_path = [_static_path+'tweetDump/cus_eng.json', _static_path+'tweetDump/cus_ger.json', _static_path+'tweetDump/cus_rus.json']
custom_header = '['
custom_tail = ']'

count = [0,0,0]
illegal = 0

json_writer = fileWriter(to_file_path,custom_header,custom_tail)
for fr in from_file_path:
    with open (fr,"r+") as f:
        for line in  f:
            if len(line) > 2 :
                try:
                    print("trying to dump :: "+line)
                    tweet = customTweet(line)
                    json_writer.dump_tweet(tweet.encode_to_json, tweet.lang)
                    if tweet.is_lang_english():
                        count[0] = count[0]+1
                    elif tweet.is_lang_german():
                        count[1] = count[1]+1
                    elif tweet.is_lang_russian():
                        count[2] = count[2]+1

                except Exception:
                    print("failed to dump :: "+line)
                    illegal+=1
                    #print("Found an illegal entry")

t=0
for f in from_file_path:
    print('Dumped :: '+f+' --> '+to_file_path[(t)])
    t=t+1
print('Write :: '+' E['+count[0]+']'+' G['+count[1]+']'+' R['+count[2]+']'+' I['+illegal+']') 