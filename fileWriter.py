import os

class fileWriter :

    _const_EN = 0
    _const_DE = 1
    _const_RU = 2
    
	file_path[_const_EN] = 'tweetDump/eng.txt'
	file_path[_const_DE] = 'tweetDump/ger.txt'
	file_path[_const_RU] = 'tweetDump/rus.txt'

	file_size[_const_EN] = 0
	file_size[_const_DE] = 0
	file_size[_const_RU] = 0
	
	writes[_const_RU] = 0
	writes[_const_DE] = 0
	writes[_const_EN] = 0
	
	def dump_tweet(tweet='{}',path='en') :
	    
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
	    
	   file_size[current_file] = os.stat(file_path[current_file]).st_size
	    
	    if file_size[current_file] <=0 :
	        write_header(file_path[current_file])
	        
	    write_tweet(file_path[current_file],tweet)
	    writes[current_file]+=1
	            
	   
    def write_header(path) : 
        with open(path,"a+") as f :
            f.write('{\n    "tweets" : [\n')
    
 '''def write_tail(path) :
        with open(path,"a+") as f :
            f.write(',\n')'''
            
    def write_eof(path) :
        with open(path,"a+") as f :
            f.seek(0,2) # 0 byte from eof
            f.write(']}')

    def write_tweet(path,tweet):
        with open(path,"a+") as f :
            f.seek(1,2) # 1 byte from eof
            if f.read(1) == '}' :
                f.seek(2,2)
                f.write(',\n')
                
            f.write(tweet)
            f.write(']}')
    
                