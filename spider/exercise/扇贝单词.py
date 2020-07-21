import requests
from urllib import request
from lxml.html import etree

words = []
def shanbei(page):

    url = "https://www.shanbay.com/wordlist/176299/521041/?page=%s"%page
    headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

    req = request.urlopen(url=url).read()
    #print(req)
    rsp = etree.HTML(req)
    #print(rsp)
    tr = rsp.xpath("//tr")
    print(len(tr))

    for i in tr:
        word = {}
        strong = i.xpath("./td/strong")
        if len(strong):
            name = strong[0].text.strip()
            word['name'] = name
            #print(name)
        to_content = i.xpath("./td[@class='span10']")
        if len(to_content):
            content = to_content[0].text.strip()
            word['content'] = content
            #print(content)

        if word!={}:
            words.append(word)

    for w in words:
        print(w)




if __name__ == '__main__':
    shanbei("1")

