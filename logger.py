from datetime import datetime
import time

_static_path = "/home/anudeep3998/cse535/code/"
file_path = _static_path+'tweetDump/log.txt'
start_time = ''
start_nano = 0
end_time = ''
end_nano = 0
elipsed_nano = 0

def start():
    global start_nano
    start_time = datetime.now().time()
    start_nano = int(round(time.time()))
    msg = "Starting twitterSiphon. \nStart Time : "+str(start_time)
    with open(file_path,"a+") as f:
        f.seek(0,2) #seek file end
        f.write("\n\n"+msg)


def end(msg):
    global start_nano
    global end_nano
    end_time = datetime.now().time()
    end_nano = int(round(time.time()))
    elipsed_nano = end_nano - start_nano
    with open(file_path,"a+") as f:
        f.seek(0,2) #seek file end
        f.write("\n"+msg+"\nFinish Time : "+str(end_time) + " Executed for : "+str(elipsed_nano)+"s")


