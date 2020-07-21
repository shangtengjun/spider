import requests
from bs4 import BeautifulSoup
from urllib import request
from lxml.html import etree
def qq():
    url = "https://hr.tencent.com/position.php?&start=10#a"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    req = request.urlopen(url=url).read()

    content = etree.HTML(req)

    print(content)
    #soup = BeautifulSoup(rsp, 'lxml')

   # print(soup)
   # div = soup.select("div[class='recruit-list']")
    #print(len(div))

    tr = content.xpath("//div")
    print(len(tr))
    for i in tr:
        name = i.xpath("a h4")[0]
        print(name)
        content = i.xpath("a p[class='recruit-text']")[0].get_text()
        print(content)



if __name__ == '__main__':
    qq()