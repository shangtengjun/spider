'''读取cookie'''
from urllib import request,parse
from http import cookiejar

#创建filecookiejar实例

cookie_jar = cookiejar.MozillaCookieJar()
cookie_jar.load('cookie.txt',ignore_expires=True,ignore_discard=True)
#创建cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie_jar)
#创建http请求管理器
http_handler = request.HTTPHandler()
#创建https管理器
https_handler = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def getHomePage():
    url = 'http://www.renren.com/972226789/profile'

    #如果已经执行了login函数，则opener自动包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('rsp4.html','w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':

    getHomePage()