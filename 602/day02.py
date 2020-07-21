# coding:utf-8
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
s = 0
for i in range(20):
    http_url = "http://tieba.baidu.com/f?kw=%E5%B9%BF%E4%B8%9C%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%E5%8D%8E%E7%AB%8B%E5%AD%A6%E9%99%A2&ie=utf-8&pn="+str(s)

    response = requests.get(http_url, headers=headers)
    html_content = response.content.decode('utf-8')
    s += 50
    r = open('.\class602\贴吧{}'.format(i+1),'w',encoding='utf-8')
    r.write(html_content)
    r.close()


'''
tu = ['https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/112/112-bigskin-1.jpg','https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/513/513-bigskin-2.jpg','https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/199/199-bigskin-2.jpg','https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/167/167-bigskin-5.jpg','https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/123/123-bigskin-2.jpg','https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/184/184-bigskin-1.jpg']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
for i in range(6):
    response = requests.get(tu[i], headers=headers)
    r = open('.\class602\图片{}'.format(i+1),'wb')
    r.write(response.content)
    r.close()
    '''
