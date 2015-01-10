#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-12-22 14:46:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
 
import _thread
from http import cookiejar
import os
import random
import re
import threading
import time
import urllib.request


userAgents = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0'},
	{"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5"},
	{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"},
	{"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)"},
	{"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0"},
	{"User-Agent":"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre"},
	{"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0"},
	{"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"},
	{"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"},
	{"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133"},
	{"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"},
	{"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"},
	{"User-Agent":"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"}, 	
	{"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"},
	{"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"},
	{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101"},
	{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}]

pics = []
urls = []
openers = []
exitFlag = 0
SAVE_DIR = "D:\\douPIC\\"

# ActivityURL = "http://www.douban.com/online/11865076/album/137771083/?start=%d&sortby=time"
# ActDir = "137771083\\"
ActivityURL = "http://www.douban.com/online/11795374/album/134727795/?start=%d&sortby=popularity"
ActDir = "11795374\\"
ActivityURL = "http://www.douban.com/photos/album/64062043/?start=%d"
ActDir = "64062043\\"

PageSize = 18

picLock = threading.Lock()
urlLock = threading.Lock()
pageNum = 0
MaxPageNum = 10

downPicCount = 10
clawThreadCount = 1


def getRandomHeaders():
    headers = []
    headers.append(("User-Agent", random.choice(userAgents)["User-Agent"]))
    headers.append(("Accept-Language", "zh-cn,zh;q=0.8;"))
    headers.append(("Cache-Control", "max-age=0"))
    headers.append(("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"))
    return headers

def initOpeners(openerCount):
    for i in range(0,openerCount):
        cj = cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = getRandomHeaders()
        urllib.request.install_opener(opener)
        openers.append(opener)
        
def getRandomOpener():
    return random.choice(openers)

def downLoadImage(url, savePath):
    testCount = 0
    while testCount < 3:
        try:
            f = getRandomOpener().open(url)
            file = open(savePath, 'wb')
            file.write(f.read())
            file.close()
            f.close() 
            break
        except Exception as e:
            print("DownLoad image %s Error:%s"%(url,str(e)))
            testCount += 1
    
    
def getHtml(url):
    testCount = 0
    html = ""
    while testCount < 3:
        try:
            f = getRandomOpener().open(url)
            html = f.read().decode('utf-8')
            f.close()
            break
        except Exception as e:
            print("getHtml %s Error:%s"%(url,str(e)))
            testCount += 1
    return html

class ClawThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global urls,pageNum
        while exitFlag == 0:
            time.sleep(0.1 * random.randint(0, 10))
            urlLock.acquire()
            pUrl = ""
            if len(urls) > 0:
                pUrl = urls[0]
                urls.remove(pUrl)
            else:
                if pageNum == MaxPageNum:
                    break
                endAddPage = pageNum + 5;
                endAddPage = min(endAddPage,MaxPageNum)
                while pageNum < endAddPage:
                    urls.append(ActivityURL % (pageNum*PageSize))
                    pageNum += 1
            urlLock.release()
            if pUrl != "":
                html = getHtml(pUrl)
                getPicURL(html)
                


class DownPicThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global urls
        while exitFlag == 0:
            time.sleep(0.01 * random.randint(0, 10))
            picLock.acquire()
            picUrl = ""
            if len(pics) > 0:
                picUrl = pics[0]
                pics.remove(picUrl)
            picLock.release()
            if picUrl != "":
                fileName = picUrl[picUrl.rindex('/')+1:]
                filePath = SAVE_DIR + ActDir + fileName
                if not os.path.exists(filePath):
                    downLoadImage(picUrl, filePath)
            else:
                if len(urls) == 0:
                    break
            

def getPicURL(html):
    reg = r"http://img3.douban.com/view/photo/thumb/public/p\d+\.jpg"
    picURLs = re.findall(reg, html)
    picLock.acquire()
    for picurl in picURLs:
        pics.append(picurl.replace("thumb", "photo"))
    picLock.release()


if __name__ == '__main__':
    
    initOpeners(10)
    
    threads = []
    
    if not os.path.exists(SAVE_DIR + ActDir):
        os.mkdir(SAVE_DIR + ActDir)
    
    for i in range(0,downPicCount):
        thread = DownPicThread("%d"%(i))
        thread.start()
        threads.append(thread)
      
    for i in range(0,clawThreadCount):
        thread = ClawThread("%d"%(i))
        thread.start()
        threads.append(thread)    
      
    while True:
        print("Downing:%d  ----------- Finished:%d"%(len(pics),len(os.listdir(SAVE_DIR + ActDir))))
        ipt = input("input 'exit' to exit:")
        if ipt == 'exit':
            exitFlag = 1
            break
      
    print("Waiting for all thread exit...")
    for thread in threads:
        thread.join()
         

