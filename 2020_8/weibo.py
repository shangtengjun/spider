import requests
import lxml.html
import re

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

#session 相当于在服务器上建立的一份用户档案，cookie 中只要存储用户的身份信息，服务器通过身份信息在 session 中查询用户的其他信息。
session = requests.Session()

#通过 session.headers.update() 方法来更新全局的 headers，通过该 session 发送的请求都会使用我们设置的全局 headers。
session.headers.update(headers)

req = session.get('https://m.weibo.cn/u/2357832895').content.decode('utf-8')

parser = lxml.html.etree.HTML(req)

infos = parser.xpath("//div[@class='m-container-max']/div[@class='profile-cover']")

print(infos)