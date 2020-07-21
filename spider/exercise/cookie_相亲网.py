"""
在线抓取相亲美女联系方式

"""
from urllib import request,parse,error
from http import cookiejar
import json

def login():
    '''
    输入登录账号和密码
    获得登录的cookie
    cookie写文件
    :return:
    '''
    #登录入口
    url = "http://www.jiayuan.com/login/dologin.php"
    #http://date.jobble.com/wp-login.php
    data = {
        "name":"15360631935",
        "password":"ddd123"
    }

    data = parse.urlencode(data)
    #存放cookie文件
    f = r'cookie.txt'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "redirect_to":"http://www.jiayuan.com/120003271?fxly=tj-jrsp-usercpv2-profile&src=usercpv2&tid=98&rid=98&index=1&reason=animal_match&algorithm=dynmatch_readmsgbaoyue_sendmsg&pid=153548875",
        "Connection":"keep-alive",
        "rememberme":"on"
    }

    cookie_hendler = cookiejar.MozillaCookieJar(f)

    http_handler = request.HTTPCookieProcessor(cookie_hendler)

    opener = request.build_opener(http_handler)

    req = request.Request(url,data=data.encode(),headers=headers)

    try:
        rsp = opener.open(req)
        cookie_hendler.save(f,ignore_discard=True,ignore_expires=True)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)

def getInfo():
    pass

if __name__ == '__main__':
    login()