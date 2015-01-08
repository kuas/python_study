#test stdout
import sys
import random
import time
import _thread
import urllib.request


def randomHeaders():
    return "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"

def downLoadImage(url,savePath):
    u = urllib.request.URLopener()
    u.addheaders = []
    u.addheader("User-Agent", randomHeaders())
    u.addheader("Accept-Language", "zh-cn,zh;q=0.8;",)
    u.addheader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    f = u.open(url)
    file = open(savePath,'wb')
    file.write(f.read())
    file.close()
    f.close()

downLoadImage("http://img3.douban.com/view/photo/photo/public/p2211076701.jpg","D://1.jpg")


## Test about thread

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("ThreadName:%s-->%s"%(threadName,time.ctime(time.time())))


##_thread.start_new_thread(print_time,("Thread-1",0.5,))
##_thread.start_new_thread(print_time,("Thread-2",0.2,))
        
'''-------------------------------drvider------------------------------------------'''

## Test about while/if
def guessNumber():
    '''Give you a random number from 0 to 100,you can guess a number,
    it where tel you next should bigger or smaller'''

    key = random.randint(0,100)
    var = -1
    time = 0
    while var != key:
        try:
            var = input("Enter a number(0-100):")
            var = int(var)
            time += 1;
            if var < key:
                print("Bigger!")
            elif var > key:
                print("Smaller!")
            else:
                print("Success,use ",time," times ");
                break;
        except Exception:
            if var == "exit":
                break
            print("Error Input",var,"!")


##guessNumber()








