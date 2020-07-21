'''使用代理访问百度'''

from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    #设置代理地址
    proxy = {'http':'218.60.8.99:3129'}
    #创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_handler)
    #安装Opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)