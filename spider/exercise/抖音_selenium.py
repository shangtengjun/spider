from selenium import webdriver
from bs4 import BeautifulSoup
import time
class Douyu():
    def setUp(self):
        self.driver = webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")
        self.url = 'https://www.douyu.com/directory/all'

    def douYu(self):
        self.driver.get(self.url)

        while True:
            soup = BeautifulSoup(self.driver.page_source,'xml')

            titles = soup.find_all('h3',{'class':'DyListCover-intro'})
            nums = soup.find_all('span',{'class':'DyListCover-hot'})

            for title,num in zip(titles,nums):
                print("房间{0}总共观赏人数{1}".format(title.get_text().strip(),num.get_text().strip()))

    def desTr(self):

        self.driver.close()
if __name__ == '__main__':
    douyu = Douyu()
    douyu.setUp()
    douyu.douYu()

    #douyu.desTr()

