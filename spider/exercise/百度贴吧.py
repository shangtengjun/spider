import requests
from urllib import parse

'''
爬取lol吧1-10页

'''
if __name__ == '__main__':
    #准备构建参数字典
    qs = {
        "kw" : "lol",
        'ie' : 'utf-8',
        'pn' : 0
    }
    urls = []
    #拼接完整url
    baseurl = 'https://tieba.baidu.com/f?'
    for i in range(10):
        qs['pn'] = str(i * 50)
        #parse编码
        urls.append(baseurl+parse.urlencode(qs))

    for url in urls:
        req = requests.get(url)
        html = req.content.decode('utf-8')
        print(url)
        print(html)
    #保存最后一个
    file = open("./百度贴吧.html",'w',encoding='utf-8')
    file.write(html)
