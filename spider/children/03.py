from urllib import request,parse
import json

baseurl = 'https://fanyi.baidu.com/sug'
#存放用来模拟form的数据一定是dict格式
cont = input()
data = {
    #值是翻译的内容，应由用户输入有准，此处使用硬编码
    'kw': cont
}
#需要使用parse模块对data进行编码
data = parse.urlencode(data).encode()
print(type(data))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    #因为使用post，至少应该包含Content-Length字段
    'Content-Length':len(data)
    }
#请求信息都封装在Request
rsp = request.Request(url=baseurl,data=data, headers=headers)
rsp = request.urlopen(rsp).read().decode()
print(type(rsp))
print(rsp)
#把json字符串转化为字典
rsp = json.loads(rsp)
print(type(rsp))
print(rsp)

for item in rsp['data']:
    print(item['k'],'--',item['v'])