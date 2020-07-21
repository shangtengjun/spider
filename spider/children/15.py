'''使用requests的post请求实现03.py的要求,对比哪个省事简单'''

import requests
import json

baseurl = 'https://fanyi.baidu.com/sug'
#存放用来模拟form的数据一定是dict格式
data = {
    #值是翻译的内容，应由用户输入有准，此处使用硬编码
    'kw': 'girl'
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    #因为使用post，至少应该包含Content-Length字段
    'Content-Length':str(len(data))
    }
#请求信息都封装在Request
rsp = requests.post(url=baseurl,data=data, headers=headers)

print(type(rsp))
print(rsp.text)
print(rsp.json())
