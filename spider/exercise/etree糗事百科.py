
import requests
from lxml.html import etree
import  json

url = "http://www.lovehhy.net/Joke/Detail/QSBK/"
uu = "http://www.foshannews.net/jtzb2016/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

req = requests.get(uu,headers=headers).content.decode('utf-8','ignore')
#print(req)
rsp = etree.HTML(req)


#content = rsp.xpath('//div[@class="post_recommend_new"]//text()')
items = []
for i in rsp.xpath('//ul[@class="mbd dot f14"]/li/a'):

    cc = i.xpath('./@href')[0].strip(".")
    title = i.xpath('./@title')[0]
    cc = "http://www.foshannews.net/jtzb2016/"+cc
    eq = requests.get (cc, headers=headers).content.decode ('utf-8', 'ignore')
    sp = etree.HTML (eq)

    cont = sp.xpath('//div[@class="TRS_Editor"]/p')
    result = {
                '标题': title,
                '标题网站': cc,

              }

    items.append(result)
rows = [['标题', '标题链接']]
print(items)
#for con in content:
    #print(con)
'''
json_strs = json.dumps(content, ensure_ascii=False, indent=2)
file = open("./糗事.json", "w",encoding="utf-8")
file.write(json_strs)
file.close()'''

