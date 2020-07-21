'''scrapy runspider spider.py -t csv -o apps.csv
# spider.py 是刚刚写的爬虫代码的文件名
# -t 表示输出的文件格式，我们用 csv，方便用 Excel 等工具打开
# -o 表示输出的文件名，所以执行完会出现一个 apps.csv 的文件'''

'''scrapy框架windows命令行一些代码'''
#让 Scrapy 创建一个名叫 appinn 项目：scrapy startproject appinn
#注意：cd 完成后检查一下自己是不是在项目的根目录：输入 explorer . 并回车打开自己所在的目录，应该可以直接看见一个 scrapy.cfg 文件；或者输入 scrapy 并回车，打印的第一句形似 Scrapy 1.7.3 - project: appinn。

#在命令行里执行下面的命令并回车，它会帮我们创建一个叫做 article 的爬虫，并且只爬取 www.appinn.com 下的网页：scrapy genspider article www.appinn.com

#在命令行输入 scrapy crawl article 并回车，爬虫就开始运行了。
#完成后我们可以在命令行里输入 explorer . 打开当前所在的 appinn 文件夹，这时我们可以找到一个名为 appin_windows_apps.csv 的文件，这就是最后的结果。


import scrapy


# 定义一个类叫做 TitleSpider 继承自 scrapy.Spider
class TitleSpider (scrapy.Spider):
    name = 'title-spider'
    # 设定开始爬取的页面,开始请求这个页面，得到一个响应。
    start_urls = ['https://www.appinn.com/category/windows/']
    #Scrapy 把这个响应交给 默认 的解析方法 parse 来处理。响应 response 就是 parse 的第一个参数。
    def parse(self, response):
        # 找到所有 article 标签
        for article in response.css ('article'):
            # 解析 article 下面 a 标签里的链接和标题
            a = article.css ('h2.title a')
            if a:
                result = {
                    'title': a.attrib['title'],
                    'url': a.attrib['href'],
                }
                # 得到结果,把这条结果告诉 Scrapy
                yield result

        # 解析下一页的链接
        next_page = response.css ('a.next::attr(href)').get ( )
        if next_page is not None:
            # 开始爬下一页，使用 parse 方法解析
            yield response.follow (next_page, self.parse)