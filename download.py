#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-12-22 14:46:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
 
import os
import urllib.request
import re
import time
import random
import _thread

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

header={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Cache-Control": "max-age=0",
        "Accept-Language": "zh-cn,zh;q=0.8;",
        "Connection": "keep-alive",
        "Host": "www.douban.com",
        "Referer": "http://www.douban.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/39.0.2171.95 Safari/537.36"
        }

def randomUserAgent():
    return random.choice(userAgents)["User-Agent"]



def downLoadImage(url,savePath):
    u = urllib.request.URLopener()
    u.addheaders = []
    u.addheader("User-Agent",randomUserAgent())
    u.addheader("Accept-Language", "zh-cn,zh;q=0.8;",)
    u.addheader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    f = u.open(url)
    file = open(savePath,'wb')
    file.write(f.read())
    file.close()
    f.close() 
 
def getHtml1(url):
    req = urllib.request.Request(url, headers = header)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    return html
 
 
def getHtml(url):
    print('*'*10,url)
    u = urllib.request.URLopener()
    u.addheaders = []
    u.addheader("User-Agent",randomUserAgent())
    u.addheader("Accept-Language", "zh-cn,zh;q=0.8;",)
    u.addheader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    f = u.open(url)
    content = f.read().decode('utf-8')
    f.close()
    return content
 
 
def getPicURL(html):
    reg = r"http://img3.douban.com/view/photo/thumb/public/p\d+\.jpg"
    #reg1 = r"http://www.douban.com/online/11865076/photo/\d+/\?sortby=time"
    picURLs = re.findall(reg, html)
    urls = []
    for picurl in picURLs:
        urls.append(picurl.replace("thumb","photo"))
    return urls
 
def openPic(picURL):
    try:
        html = getHtml(picURL)
        reg = r'<img src="http://img\d{1}.douban.com/view/photo/photo/public/p\d{10}\.jpg"'
        picURL = re.findall(reg, html)
        #print(picURL)
        picURL_open = picURL[0].split('"')
    except:
        print("openPic Error:")
    return picURL_open[1]
 
def picDownload(picURLs, page_num):
    download_img = ''
    dirs = os.listdir("D:\\douPIC")
    for picURL in picURLs:
        try:
            #picURL_new = openPic(picURL)
            if picURL[-15:] not in dirs:
                file_name = picURL[-15:]
                
                downLoadImage(picURL, "D:\\douPIC\\%s" % (file_name))
                #download_img = urllib.request.urlretrieve(picURL, "D:\\douPIC\\%s" % (file_name))
                dirs.append(file_name)
                print("第%d页 第%d张 ......%s......... downloaded" % (page_num+1, picURLs.index(picURL)+1, picURL[-15:]))
            else:
                print("第%d页 第%d张 ......%s......... existed" % (page_num+1, picURLs.index(picURL)+1, picURL[-15:])) 
            
        except:
            print("Download Error:%s"%(picURL_new))
    return download_img
 
if __name__ == '__main__':
    num = 0
    page_num = 0
    #downLoadImage("http://img3.douban.com/view/photo/photo/public/p2211076701.jpg","D://1.jpg")
    while True:
        html = getHtml(r'http://www.douban.com/online/11865076/album/137771083/?start=%d&sortby=time' % (num+page_num*90))
        picURLs = getPicURL(html)
        print("**************第%d页下载开始***************" % (page_num+1))
        picDownload(picURLs, page_num)
        print("**************第%d页下载完成***************" % (page_num+1))
        page_num += 1
