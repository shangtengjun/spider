# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Question(scrapy.Item):
    title = scrapy.Field()        # 提问标题
    link = scrapy.Field()         # 提问链接
    question_id = scrapy.Field()  # 问题 id，为了可以把提问和回答关联起

class Answer(scrapy.Item):
    author = scrapy.Field()       # 作者
    vote_count = scrapy.Field()   # 赞同数
    content = scrapy.Field()      # 回答内容
    question_id = scrapy.Field()  # 问题 id，为了可以把提问和回答关联起来