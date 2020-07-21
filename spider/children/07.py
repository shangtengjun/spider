'''自动使用cookie，自动登录'''

from urllib import request,parse
from http import cookiejar

#创建cookiejar实例
cookie_jar = cookiejar.CookieJar()
#创建cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie_jar)
#创建http请求管理器
http_handler = request.HTTPHandler()
#创建https管理器
https_handler = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名，密码，用来获取cookie凭证
    '''

    #此url需要从登录form的action属性提取
    url = 'http://www.renren.com/PLogin.do'

    #此键值需要从登录form的两个input中提取name属性
    data = {
        "email":'15360631935',
        "password":'ddd123'
    }

    #把数据进行编码
    data = parse.urlencode(data)

    #创建一个请求对象
    req = request.Request(url=url,data=data.encode())

    #使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'http://www.renren.com/972226789/profile'

    #如果已经执行了login函数，则opener自动包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('rsp3.html','w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()