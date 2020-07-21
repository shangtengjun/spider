import requests
import useragentutil
import proxypool
import lxml.html
import os
import json

#面向对象
class OfferIndexSpider(object):
    def __init__(self):
        #初始化操作
        self.offer_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&add"

    def parse_offer_url(self):
        """解析网址,获取源码信息"""
        offer_response = requests.get(self.offer_url,headers=useragentutil.get_headers(),proxies=proxypool.get_proxy())
        html = offer_response.content.decode("gbk")
        return html

    def run(self):
        offer_html_datas = self.parse_offer_url()
       # print(offer_html_datas)

    def catch_list(self):
        """提取数据内容"""
        # 定义变量
        list = []
        # （1）解析器对象； --用于解析html代码
        metree = lxml.html.etree
        proxy_parser = metree.HTML (self.parse_offer_url())
        # （2）获得所有的el列表；
        tr_list = proxy_parser.xpath ("//div[@class='el']")
        # （3）遍历el列表，el单个元素；
        for tr_element in tr_list:
            item = {}
            # （4）提取数据内容；
            # 工作岗位
            workname = tr_element.xpath ("./p/span/a/text()")
            workname = "".join(workname).strip()
            item["workname"] = workname
            #公司名
            company = tr_element.xpath ("./span[@class='t2']/a/text()")
            company = "".join(company)
            item["companyname"] = company
            # 地点
            place = tr_element.xpath ("./span[@class='t3']/text()")
            place = "".join(place)
            item["place"] = place
            #薪资
            gallery = tr_element.xpath ("./span[@class='t4']/text()")
            gallery = "".join(gallery)
            #gallery[0] if len(gallery)>0 else "4-6k"
            item["monney"] = gallery
            #时间
            time = tr_element.xpath ("./span[@class='t5']/text()")
            time = "".join(time)
            item["time"] = time
            #岗位链接
            worklink = tr_element.xpath ("./p/span/a/@href")
            worklink = "".join (worklink)
            item["worklink"] = worklink
            #公司链接
            cplink = tr_element.xpath ("./span[@class='t2']/a/@href")
            cplink = "".join (cplink)
            item["cplink"] = cplink

            list.append (item)

        return list

    def save_file(self):
        """保存所有的数据到json文件中"""
        # 保存文件
        ip_path = "./ip_path"
        if not os.path.exists (ip_path):
            os.makedirs (ip_path)
        json.dump (self.catch_list(),
                   open (ip_path + "/work.json", "w", encoding="utf-8"),
                   ensure_ascii=False,
                   indent=2)
        print ("所有数据已保存成功")



def main():
    spider = OfferIndexSpider()
    #spider.save_file()


if __name__ == '__main__':
    main()