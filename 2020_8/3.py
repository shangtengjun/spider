import requests
from lxml.html import etree
session = requests.Session()
headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
      'Cookie': 'csrf_weiyangx_cookie=e997a31df5a45b910a49931417078425; UM_distinctid=173ecdfa24b144-00ca1d867da36c-4353761-144000-173ecdfa24c6cb; _weiyangx_product_=jjf1rcck352i7sba16v05247apffa2i1; CNZZDATA1270867928=1395282097-1597402939-%7C1597408346',
    }
Form_data = {
    'phone': '13192862027',
    'password': 'DDD123'
}

session.headers.update(headers)

req = session.post('https://www.liepin.com/zhaopin/',data=Form_data).content.decode('utf-8')

rsp = etree.HTML(req)

print(rsp.xpath("//div[@class='uk-grid uk-grid-small']"))
