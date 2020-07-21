'''
下载页面
提取每部电影信息在<dd> </dd>
对每个dd进行提取信息
'''
import re
import requests

url = "https://maoyan.com/board"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

rsp = requests.get(url=url,headers=headers)
html = rsp.content.decode()
print(html)

s = r'<dd>(.*?)</dd>'

pattern = re.compile(s,re.S)

films = pattern.findall(html)

print(len(films))

for film in films:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)
    s2 = r'<p.*?>(.*?)</p>'
    pattern2 = re.compile(s2)
    star = pattern2.findall(film)[1]
    print(star)
