
import requests
from lxml.html import etree
import  json

url = "http://www.lovehhy.net/Joke/Detail/QSBK/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

req = requests.get(url,headers=headers).content.decode('GBK','ignore')
#print(req)
rsp = etree.HTML(req)


content = rsp.xpath('//div[@class="post_recommend_new"]//text()')
#print(content)
for con in content:
    print(con)

json_strs = json.dumps(content, ensure_ascii=False, indent=2)
file = open("./糗事.json", "w",encoding="utf-8")
file.write(json_strs)
file.close()

