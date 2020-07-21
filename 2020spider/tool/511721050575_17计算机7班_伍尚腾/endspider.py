import requests
import lxml.html
import re
import useragentutil
import proxypool
import time
import random
import os
import xlwt


class OfferSpider(object):
    def __init__(self):
        """初始化操作"""
        # 首页 url
        self.offer_index_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?lang=c&postchannel=0000&workyear=99 &cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        self.offer_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,{}.html?lang=c&postchannel=0000&workyear=99 &cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        self.offer_datas = []

    def get_offer_pages(self):
        """动态获取页面数,int"""
        offer_page_response = requests.get(self.offer_index_url,headers=useragentutil.get_headers( ),proxies=proxypool.get_proxy( ))
        # 获取网页源码
        page_html_content = offer_page_response.content.decode("gbk")
        # 解析数据
        metree = lxml.html.etree
        page_parser = metree.HTML(page_html_content)
        # 获得内容值
        pages_content = page_parser.xpath("//div[@class='dw_page']//span[@class='td']/text()")[0]
        pages = int(re.search(r"共(\d+)页",pages_content)[1])
        return pages

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
        offer_html_content = offer_response.content.decode("gbk")
        # 限制处理
        wait_time = random.randint(0,10)
        print("动态限制访问频率,%ds 后继续爬取数据..."%wait_time)
        time.sleep(wait_time)
        return offer_html_content

    def catch_work_info(self, temp_url):
        """提取工作职责信息"""
        try:
            work_response = requests.get(temp_url, headers=useragentutil.get_headers(), proxies=proxypool.get_proxy())
            work_html_content = work_response.content.decode("gbk")
            work_parser = lxml.html.etree.HTML(work_html_content)
            work_infos = "".join(work_parser.xpath ("//div[@class='bmsg job_msg inbox']//text()")).strip( ).replace(" ","")  # 清洗数据
            #print("工作职责:",work_infos)
        except Exception:
            work_infos = "暂无数据"
        return work_infos

    def catch_company_info(self, temp_url):
        """提取公司简介信息"""
        try:
            company_response = requests.get(temp_url, headers=useragentutil.get_headers(), proxies=proxypool.get_proxy())
            company_html_content = company_response.content.decode("gbk")
            # 提取数据
            company_parser = lxml.html.etree.HTML(company_html_content)
            company_infos = "".join(company_parser.xpath("//div[@class='con_txt']//text()")).strip( ).replace(" ", "")
        except Exception:
            company_infos = "暂无数据"
        return company_infos

    def catch_offer_lists(self, html_content):
        """提取所有页面的岗位信息"""
        metree = lxml.html.etree
        # 处理
        offer_parser = metree.HTML(html_content)
        div_list = offer_parser.xpath("//div[@id='resultList']/div[@class='el']")
        # 遍历
        for div_element in div_list:
            # 工作岗位
            offer_item = []
            # 职位名、职位名称链接、公司名、公司链接、工作地点、薪资、发布时间、工作职责、公司简介 -->职位的工作职责/公司简介
            #职位名
            position = div_element.xpath("./p/span/a/text()")[0]
            offer_item.append(position.strip( ))
            # 职位名称链接
            position_url = div_element.xpath("./p//a/@href")[0]
            offer_item.append(position_url)
            # 公司名
            company = div_element.xpath("./span[@class='t2']/a/@title")[0]
            offer_item.append(company)
            # 公司链接
            company_url = div_element.xpath("./span[@class='t2']/a/@href")[0]
            offer_item.append(company_url)
            # 工作地点
            work_loc = div_element.xpath("./span[@class='t3']/text()")[0]
            offer_item.append(work_loc)
            # 薪资 --IndexError --出现异常,异常处理!--跳开程序崩溃!
            salary_value = div_element.xpath("./span[@class='t4']/text()")
            #print(salary_value)
            salary = salary_value[0] if len(salary_value)>0 else"4-6 千/月"
            #offer_item.append(salary)
            salary_result = 8000
            if "千/月" in salary:
            # 4-6 千/月
                salary_result = int(float(salary.split("-")[0])*1000)
            elif "万/月" in salary:
                salary_result = int(float(salary.split("-")[0])*10000)
            elif "万/年" in salary:
                salary_result = int(float(salary.split("-")[0])/12*10000)
            offer_item.append(salary_result)

            # 发布时间
            public_time = div_element.xpath("./span[@class='t5']/text()")[0]
            offer_item.append(public_time)
            # 工作职责
            work_informations = self.catch_work_info(position_url)
            offer_item.append(work_informations)
            #公司简介
            company_informations = self.catch_company_info(company_url)
            offer_item.append(company_informations)
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
        offer_sheet = book.add_sheet("Python 招聘信息")
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
            book.save(offer_path+"/招聘 Python 岗位信息表.xls")
        print("所有数据已保存成功!!!")

    def run(self):
        """启动程序"""
        excel_titles = ["职位名","职位名称链接","公司名","公司链接","工作地点","薪资","发布时间","工作职责","公司简介"]
        self.offer_datas.append(excel_titles)
        # 动态获取页面数
        #page_total = self.get_offer_pages()
        page_total = 20
        #拼接所有页面
        offer_url_lists = self.get_offer_url_list(page_total)
        #爬取所有页面内容，每循环一次爬取新一页
        for offer_url_list in offer_url_lists:
            parse_content = self.parse_offer_url(offer_url_list)
            self.catch_offer_lists(parse_content)

        #保存数据到excel
        self.save_offer_file()


def main():
    spider = OfferSpider( )
    spider.run()

if __name__ == '__main__':
    print(os.getcwd())
    main()