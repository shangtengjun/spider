'''
爬取豆瓣电影数据
了解Ajax的基本爬取方式
'''

import json
from urllib import request

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
req = request.Request(url=url,headers=headers)
req = request.urlopen(req)

rsp = req.read().decode()

print(rsp)

data = json.loads(rsp)
print(data)