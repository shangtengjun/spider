'''requests使用代理访问百度,c参考05.py'''

import requests

if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    #设置代理地址
    proxy = {'http':'218.60.8.99:3129'}


    rsp = requests.get(url=url,proxies=proxy)
    html = rsp.text
    print(html)
