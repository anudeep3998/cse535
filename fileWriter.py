import os

_const_EN = 0
_const_DE = 1
_const_RU = 2
file_path = ['tweetDump/eng2.txt', 'tweetDump/ger2.txt', 'tweetDump/rus2.txt']
file_size = [0,0,0]
writes = [0,0,0]
_size_linesep = len(os.linesep)

class fileWriter :
	
    def write_header(self, path) : 
        with open(path,"a+") as f :
            f.write('{\n    "tweets" : [')


    '''def write_tail(path) :
        with open(path,"a+") as f :
            f.write(',\n')'''

    def write_eof(self, path) :
        with open(path,"a+") as f :
            f.seek(0,2) # 0 byte from eof
            f.write(']}')

    def write_tweet(self, path,tweet):
        global _size_linesep
        with open(path,"a+") as f :
            f.seek(0,2) # goto start of file
            f.seek(f.tell() - (_size_linesep+1),0)
            '''print(f.read(2))
            print(f.read(1))
            print(f.read(1))'''
            if f.read(1) == ']' :
                f.seek(f.tell()-2,0)
                f.truncate()
                f.write(',\n')
                
            f.write(tweet)
            f.write(']}')
    
    def dump_tweet(self, tweet='{}',path='en') :
	    
	    global _const_RU
	    global _const_DE
	    global _const_EN
	    global file_size
	    global file_path
	    global writes
	    
	    current_file = _const_EN
	    
	    if 'en' == path :
	        current_file = _const_EN
	        #en_file_size = os.stat(en_file_path).st_size
	    elif 'de' == path :
	        current_file = _const_DE
	        #de_file_size = os.stat(de_file_path).st_size
	    elif 'ru' == path :
	        current_file = _const_RU
	        #ru_file_size = os.stat(ru_file_path).st_size
	    else :
	        raise ValueError("Illegal tweet language")
	        
	    
	    #check file size to determine whether header text needs to be added and cache
	    
	    try:
	        file_size[current_file] = os.stat(file_path[current_file]).st_size
	    except FileNotFoundError:
	        file_size[current_file] = 0
	    finally:
	        if file_size[current_file] <=0 :
	            self.write_header(file_path[current_file])
	    
	    
	    
	        
	    self.write_tweet(file_path[current_file],tweet)
	    writes[current_file]+=1