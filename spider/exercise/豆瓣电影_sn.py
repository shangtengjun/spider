from selenium import webdriver
import time
from lxml.html import etree

def get_web(url):
    driver = webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")
    driver.get(url)

    time.sleep(6)
    #截图
    driver.save_screenshot('douban_reader.png')

    fn = 'douban_reader.html'

    with open(fn,'w',encoding='utf-8') as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()

def content_parse(fn):

    with open(fn,'r',encoding='utf-8') as f:
        html = f.read()
    # 生成xml
    tree = etree.HTML(html)

    books = tree.xpath("//div[@class='item-root']")

    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        print(book_name[0].text)

if __name__ == '__main__':
    url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0"

    get_web(url)