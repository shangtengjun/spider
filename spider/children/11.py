'''强行访问不安全网站，ssl'''

from urllib import request
import ssl
#利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
req = request.Request(url=url,headers=headers)
rsp = request.urlopen(req)
html = rsp.read().decode()
print(html)