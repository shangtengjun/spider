import urllib.request
import chardet
#入口
if __name__ == '__main__':
    #爬取网页地址
    url = 'https://www.bilibili.com/'
    #隐藏爬虫身份
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    rsp = urllib.request.Request(url=url,headers=headers)


    html = urllib.request.urlopen(rsp).read()
    #chardet自动检测编码格式
    cs = chardet.detect(html)
    #使用get取值保证不会出错，取不到就按默认
    html = html.decode(cs.get('encoding','utf-8'))

    print(cs)
    print(html)