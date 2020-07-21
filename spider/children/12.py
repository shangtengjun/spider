'''破解有道词典,处理js加密代码'''
'''
找到js的操作代码
salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
sign = n.md5("fanyideskweb" + e + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
'''
from urllib import request,parse
import time,random
import hashlib
import ssl
import requests
from io import BytesIO
import gzip

#利用非认证上下文环境替换认证的上下文环境
#ssl._create_default_https_context = ssl._create_unverified_context

def getSalt():
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt

def getMD5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))

    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)
    return sign



def youdao(key):
     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
     salt = getSalt()
     data = {
         'i': key,
         'from': 'AUTO',
         'to': 'AUTO',
         'smartresult': 'dict',
         'client': 'fanyideskweb',
         'salt': str(salt),
         'sign': getSign(key,salt),
         'ts': '1568718025978',
         'bv': 'a4f4c82afd8bdba188e568d101be3f53',
         'doctype': 'json',
         'version': '2.1',
         'keyfrom': 'fanyi.web',
         'action': 'FY_BY_REALTlME'
     }

     data = parse.urlencode(data).encode()

     headers = {

         'Accept': 'application/json,text/javascript,*/*;q=0.01',
         'Accept-Encoding': 'gzip,deflate',
         'Accept-Language': 'zh-CN,zh;q=0.9',
         'Connection': 'keep-alive',
         'Content-Length': len(data),
         'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
         'Cookie':'td_cookie=18446744071198736582;OUTFOX_SEARCH_USER_ID=-1629902163@10.169.0.84;SESSIONID=aaa4OHG7p56qs-FFq4_0w;OUTFOX_SEARCH_USER_ID_NCOO=1645687119.969485;___rl__test__cookies=1568718133906',
         'Host': 'fanyi.youdao.com',
         'Origin': 'http://fanyi.youdao.com',
         'Referer':'http://fanyi.youdao.com /',
         'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/76.0.3809.132 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'

     }

     req = request.Request(url=url,headers=headers,data=data)
     rsp = request.urlopen(req)
     html = rsp.read()
     #html = html.decode('utf-8',errors='ignore')
     buff = BytesIO(html)

     f = gzip.GzipFile(fileobj=buff)

     res = f.read().decode('utf-8')

     print(res)

     #html = requests.get(url,headers=headers,data=data)
     #html = html.content

     #print(html)

if __name__ == '__main__':
    youdao('beautiful')