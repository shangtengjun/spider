'''
使用requests模块，研究返回结果
'''

import requests
#完整访问的url是加后面参数
url = 'http://www.baidu.com/s?'

kw = {
    'wd':'王八蛋'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

rsp = requests.get(url,headers=headers,params=kw)

print(rsp.text)
print(rsp.content)
print(rsp.status_code)