

from urllib import request,error
import random

if __name__ == '__main__':

    url = 'http://www.baidu.com/'

    #设置代理地址
    proxy_list = [
        {'http': '111.29.3.224:8080'},
        {'http': '39.137.69.10:8080	'},
        {'http': '221.178.232.130:8080	'}
    ]

    #创建ProxyHandler
    proxy_handler_list = []
    for proxy in proxy_list:
        proxy_handler = request.ProxyHandler(proxy)
        proxy_handler_list.append(proxy_handler)

    #创建Opener
    opener_list = []
    for proxy_handler in proxy_handler_list:
        opener = request.build_opener(proxy_handler)
        opener_list.append(opener)



    try:
        op = random.choice(opener_list)
        # 安装Opener
        request.install_opener(op)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)