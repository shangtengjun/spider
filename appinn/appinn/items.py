# Define here the models for your scraped items
#items.py 是记录我们想要的数据格式的文件。在确定了我们要爬的数据是什么之后，就可以来定义数据的格式。
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#在爬取网页的时候常常出现数据缺失、内容错误之类的问题，使用 Item 可以更好的处理这些问题。

class AppinnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Article(scrapy.Item):
    title = scrapy.Field()    # 标题
    time = scrapy.Field()     # 时间
    author = scrapy.Field()   # 作者
    score = scrapy.Field()    # 分数
    content = scrapy.Field()  # 内容
