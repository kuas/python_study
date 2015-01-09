# coding:utf-8
#!python 2.7
import sys, os
import urllib2
import time
from threading import Thread
from BeautifulSoup import BeautifulSoup
import random

urlRoot = 'http://20pwww.vvvv12.com'
#urlRoot = 'http://uuu.11com137aa.comwww.vvvv12.com'		# 这个不行就用上面的那个,替换时记得注释掉这行.
sPage = 264		# 开始页数
ePage = 264		# 结束页数(页数少下载完成的快,页数多下载完成的慢)
downCount = 10	# 每页下载检查的次数(有时下载会失败,让它多跑几次,但不会重复下载已经下载过的网页源码和图片)

headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0'},
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

# 随机一个header
def randomHeaders():
	return random.choice(headers)

# 抓网页源码,并返回为str
def getHtmlSrc(url, header):
	req = urllib2.Request(url, header)
	res = urllib2.urlopen(url, timeout=60)
	htmlSrc = res.read()
	res.close
	return htmlSrc

# 把抓到的网页源码保存到txt文本中
def saveHtmlSrc(url, fileName):
		start = time.time()
		if not os.path.exists(fileName):	# 控制是否要下载
			header = randomHeaders()
			try:		
				html = getHtmlSrc(url, header)
				with open(fileName,'w') as f:
					f.write(html)
					print url
			except Exception:
				print url
				print "[-] Bad Header: ",header
				print "Time: %s s" % (time.time() - start)

# 读抓到的page页源码,获取这个page页中有几条子页面,返回一个子页面链接的list
def getChildUrls(fileName, url):
	childUrlList = []
	with open(fileName,'r') as f:
		bs = BeautifulSoup(f)
		hrefs = bs.findAll('a')
		for href in hrefs:
			hUrl = href.get('href')
			if hUrl is not None and hUrl[:4] == '/htm':
				childUrlList.append(url+hUrl)
		print 'Urls : ',len(childUrlList)
		return childUrlList

# 读子页面的源码,获取里面的图片链接,返回一个图片链接list
def getImgUrls(fileName):
	imgUrlList = []
	with open(fileName,'r') as f:
		bs = BeautifulSoup(f)
		hrefs = bs.findAll('img')
		for href in hrefs:
			imgUrl = href.get('src')
			if imgUrl[:4] == 'http':	# 图片链接是否符合
				imgUrlList.append(imgUrl)
		print 'Urls : ',len(imgUrlList)
		return imgUrlList

# 下载图片保存到指定路径
def saveImg(imgUrl ,imgFile):
	start = time.time()	
	if not os.path.exists(imgFile):	# 控制是否要下载
		header = randomHeaders()
		try:
			req = urllib2.Request(imgUrl, header)
			res = urllib2.urlopen(imgUrl, timeout=60)
			pic = res.read()
			with open(imgFile, "wb") as f:
				f.write(pic)
				print imgUrl
				# print imgFile
		except Exception:
			print imgUrl
			print "[-] Bad Header: ",header
			print "Time: %s s" % (time.time() - start)

# 获取页面title
def getHtmlTile(fileName):
	with open(fileName, "r") as f:
		bs = BeautifulSoup(f)
		return urllib2.unquote(str(bs.title.string).split('-')[0]).decode('utf-8', 'ignore').encode('gbk', 'ignore')

# 保存页面thread
class CatchSaveHtml(Thread):
	def __init__(self, url, fileName):
		Thread.__init__(self)
		self.url = url
		self.fileName = fileName

	def run(self):
		saveHtmlSrc(self.url, self.fileName)

# 保存图片thread
class CatchSaveImg(Thread):
	def __init__(self, url, imgFile):
		Thread.__init__(self)
		self.url = url
		self.imgFile = imgFile

	def run(self):
		saveImg(self.url, self.imgFile)

if __name__ == '__main__':
	for page in range(sPage,ePage+1):	# 下载的page范围
		print '>'*40+(' Page %d ' % page)+'<'*40
		urlPage = urlRoot+'/p01/list_%d.html' % page	# page页的url
		for i in range(downCount):		# 每页下载的幅度
			print '>'*38+(' Down Count %d ' % i)+'<'*38
			dirPathHtml = os.path.join(sys.path[0],'html',str(page))	# html源码保存的目录
			if not os.path.exists(dirPathHtml):		# dirPathHtml不存在
				os.makedirs(dirPathHtml)			# 创建dirPathHtml目录,只会执行一次
			pageHtmlFile = os.path.join(dirPathHtml,'%s.html' % str(page))	# page页源码文件的完整路径
			if not os.path.exists(pageHtmlFile):		# pageHtmlFile不存在
				start = time.time()
				saveHtmlSrc(urlPage, pageHtmlFile)		# 下载page页源码保存到pageHtmlFile里
				print "Total time: %s" % (time.time() - start)
			else:	# pageHtmlFile已存在
				print dirPathHtml
				childUrlList = getChildUrls(pageHtmlFile, urlRoot)	# 获取page页内的子链接列表
				if len(childUrlList) > 0:	# 有子链接
					start = time.time()
					print 'Files: ',sum([len(files) for root,dirs,files in os.walk(dirPathHtml)]) - 1	# 显示目前已下载的子链接文件数量,减1是为了去掉page页的源码文件(它们是保存在一个目录下的)
					for childUrl in childUrlList:	# 多线程下载子链接的html源码
						childHtmlName = childUrl.split('/')[-1]		# 子链接.html文件名是一个数字或字母不需要字符集转换
						childHtmlFile = os.path.join(dirPathHtml,childHtmlName)	# 子链接源码文件的完整路径
						cHtml = CatchSaveHtml(childUrl, childHtmlFile)
						cHtml.start()
					cHtml.join()
					print "Total time: %s" % (time.time() - start)

					for childUrl in childUrlList:	# 遍历子链接
						childHtmlFile = os.path.join(dirPathHtml,childUrl.split('/')[-1])	# 子链接源码文件的完整路径
						if os.path.exists(childHtmlFile):		# childHtmlFile存在
							imgUrls = getImgUrls(childHtmlFile)	# 获取子链接内的图片链接列表
							if len(imgUrls) > 0:	# 有图片
								start = time.time()
								dirPathPagePic = os.path.join(sys.path[0],'pic',str(page))	# 整个page的图片存放负的根目录
								if not os.path.exists(dirPathPagePic):		# dirPathPagePic目录不存在
									os.makedirs(dirPathPagePic)				# 创建dirPathPagePic目录
								# dirName = getHtmlTile(childHtmlFile)	# 图片的父目录名(来自html的标题title)
								dirName = urllib2.unquote(str(imgUrls[0].split('/')[-2])).decode('utf-8', 'ignore').encode('gbk', 'ignore')	# 图片的父目录名(取的imgUrls列表第一个链接,所有的url链接前半部分是一样的)
								dirPathImg = os.path.join(dirPathPagePic,dirName)	# 图片存放的完整目录
								if not os.path.exists(dirPathImg):	# dirPathImg不存在
									os.makedirs(dirPathImg)			# 创建dirPathImg
								print 'Files: ',sum([len(files) for root,dirs,files in os.walk(dirPathImg)])	# 显示当前子链接内已下载的图片数量
								for imgUrl in imgUrls:	# 多线程下载子链接内的图片
									imgFileName = os.path.join(dirPathImg,str(imgUrl.split("/")[-1]))	# 图片文件存放的完整路径名,图片名是一个数字或字母不需要字符集转换
									cImg = CatchSaveImg(imgUrl, imgFileName)
									cImg.start()
								cImg.join()
								print "Total time: %s" % (time.time() - start)
