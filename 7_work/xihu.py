import requests
import lxml.html
import re
import useragentutil
import proxypool
import time
import random
import os
import xlwt
from PIL import Image
import pytesseract


class OfferSpider(object):
    def __init__(self):
        """初始化操作"""
        # 首页 url
        self.offer_index_url = "http://www.cnxhyp.com/sell/list-351.html"
        self.offer_url = "http://www.cnxhyp.com/sell/list-351-{}.html"
        self.offer_datas = []

    def get_offer_url_list(self, numbers):
        """拼接所有的页面 url"""
        url_list = []
        for page_index in range(1, numbers + 1):
            temp_url = self.offer_url.format(page_index)
            # 添加到列表
            url_list.append(temp_url)
        return url_list

    def parse_offer_url(self, temp_url):
        """爬取整个页面内容"""
        offer_response = requests.get(temp_url,headers=useragentutil.get_headers(), proxies=proxypool.get_proxy())
        offer_html_content = offer_response.content.decode("utf-8")
        # 限制处理
        wait_time = random.randint(0,5)
        print("动态限制访问频率,%ds 后继续爬取数据..."%wait_time)
        time.sleep(wait_time)
        return offer_html_content

    def catch_work_info(self, temp_url):
        """提取工作职责信息"""
        try:
            work_response = requests.get(temp_url, headers=useragentutil.get_headers(), proxies=proxypool.get_proxy())
            work_html_content = work_response.content.decode("utf-8")

            work_parser = lxml.html.etree.HTML(work_html_content)
            work_infos = work_parser.xpath("//div[@class='tabs_box pllist active']//ul[@class='clearfix']/li")
            url = []
            for li in work_infos:
                url.append(li.xpath("./a/@href"))


        except Exception:
            work_infos = "暂无数据"

        return url

    def catch_offer_lists(self, html_content):
        """提取所有页面的岗位信息"""
        metree = lxml.html.etree
        # 处理
        offer_parser = metree.HTML(html_content)
        offer_item = []

        cp_name = offer_parser.xpath("//div[@id='contact']//div[@class='about_info iconboxAll']/h3/text()")[0]
        offer_item.append(cp_name.strip())


        s_name = offer_parser.xpath("//div[@class='black f16']/h1/text()")[0]
        offer_item.append(s_name.strip( ))

        name = offer_parser.xpath("//div[@id='contact']/div[@class='ml10 mt10 clearfix']/div/text()")[1]
        name = name.strip ( ).split (r"（")[0]
        if name.isdigit():
            offer_item.append ("未备注姓名")
        else:
            offer_item.append(name)

        p = offer_parser.xpath("//div[@id='contact']/div[@class='ml10 mt10 clearfix']/p")
        if 2 == int(len(p)):
            phone = offer_parser.xpath("//div[@id='contact']/div[@class='ml10 mt10 clearfix']/p/img/@src")[1]
        elif int(len(p))==1:
            phone = offer_parser.xpath ("//div[@id='contact']/div[@class='ml10 mt10 clearfix']/p/img/@src")[0]
        else:
            phone = 'http://www.cnxhyp.com/api/image.png.php?auth=8e59p7CdwkARbg9ckaSIZnCmcsmvFULBV1JKM3BJKqD8xqbcDfWwafFQ5w'

        url = phone

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'http://www.cnxhyp.com/sell/show-2702.html'

        }
        req = requests.get(url, headers=headers, proxies=proxypool.get_proxy())
        rsp = req.content
        f = open("./tupian.png", 'wb')
        f.write (rsp)
        f.close ( )
        image = Image.open('./tupian.png')
        content = pytesseract.image_to_string(image)  # 解析图片
        offer_item.append(content)





        print(offer_item)
        self.offer_datas.append(offer_item)

    def save_offer_file(self):
        """保存所有的数据内容到 Excel 中"""
        offer_path = "./lastoffer"
        if not os.path.exists(offer_path):
            os.mkdir(offer_path)
        # 获得 Book 工作簿
        book = xlwt.Workbook(encoding="utf-8")
        # 创建一个表格标题
        offer_sheet = book.add_sheet("洗护行业信息")
        # 写入数据
        # 行、列
        row_index = 0
        while row_index < len(self.offer_datas):
            # 列
            col_index = 0
            while col_index<len(self.offer_datas[row_index]):
                #写入数据
                offer_sheet.write(row_index,col_index,self.offer_datas[row_index][col_index])
                col_index += 1
            row_index += 1
            # 保存数据结果
            book.save(offer_path+"/洗护行业信息表.xls")
        print("所有数据已保存成功!!!")

    def run(self):
        """启动程序"""
        excel_titles = ["公司名", "产品名", "联系人", "联系电话"]
        self.offer_datas.append(excel_titles)
        # 动态获取页面数
        # page_total = self.get_offer_pages()
        page_total = 30
        # 拼接所有页面
        offer_url_lists = self.get_offer_url_list(page_total)
        # 爬取所有页面内容，每循环一次爬取新一页
        c = 0
        for offer_url_list in offer_url_lists:
            print(c)
            url = self.catch_work_info(offer_url_list)
            for u in url:
                parse_content = self.parse_offer_url(u[0])
                self.catch_offer_lists(parse_content)
            c += 1



        # 保存数据到excel
        self.save_offer_file( )

def main():
    spider = OfferSpider( )
    spider.run( )

if __name__ == '__main__':

    main( )