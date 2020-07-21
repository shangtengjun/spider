import scrapy
from appinn.items import Article

class ArticleSpider(scrapy.Spider):
    #name 是项目中每个爬虫唯一的名字，用来区分不同的爬虫
    name = 'article'
    #allowed_domains是允许爬取的域名，如果请求的链接不在这个域名下，那么这些请求将会被过滤掉。
    allowed_domains = ['www.appinn.com']
    #start_urls 是初始请求地址的列表，也就是一开始就爬取的页面地址列表。
    start_urls = ['http://www.appinn.com/category/windows/']

    #parse() 方法是默认的解析方法，负责解析返回的响应、提取数据或者生成下一步要处理的请求。
    def parse(self, response):
        # 找到所有文章的链接，通知 Scrapy 用 parse_article 方法解析
        for article_url in response.css ('article h2.title a::attr(href)').getall ( ):
            if not article_url:
                continue
            # 后续请求和解析
            yield response.follow (article_url, self.parse_article)

        # 找到下一页的链接，通知 Scrapy 用 parse 方法解析
        next_page = response.css ('a.next::attr(href)').get ( )
        if next_page:
            # 后续请求和解析
            yield response.follow (next_page, self.parse)

    def parse_article(self, response):
        article = Article ( )
        # 从 response 里提取出标题、时间、作者、分数和内容
        # 并将它们都存到 artile 这个 item 里
        article['title'] = response.css ('h1.title::text').get ( )
        article['time'] = response.css ('span.thetime span::text').get ( )
        article['author'] = response.css ('span.theauthor span a::text').get ( )
        article['score'] = response.css ('em strong::text').get ( )
        contents = response.css ('div.post-single-content *::text').getall ( )
        article['content'] = '\n'.join (contents)
        # 给出结果
        #yield，它和 return 类似，但不会结束函数或方法，而能够多次返回内容。
        yield article
