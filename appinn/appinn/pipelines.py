# Define your item pipelines here
#pipelines.py 文件允许我们在得到结果之后，对结果进行一些处理。比如我们不想要分数在 3 以下的文章，就可以在 pipelines.py 里面做处理。
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

#Scrapy 替我们自动生成的代码如下，默认会直接 return item，意思是保留所有的 item
class AppinnPipeline:
    #这个 process_item() 方法就是得到结果之后处理 item 的方法，在这里做一些过滤或者对 item 做一些修改都是可以的。
    def process_item(self, item, spider):
        if item.get ('score'):
            # 把 item 的 score 变成整数
            item['score'] = int(item['score'])
            #在这个方法里 raise DropItem() 可以去掉我们不想要的 item，所以我们把它改成下面这样来去掉 3 分以下的文章
            if item['score'] < 3:
                raise DropItem ('去掉 3 分以下的文章')
        return item
