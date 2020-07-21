from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content,'lxml')

'''css选择'''
titles = soup.select('title')
print(titles)
print('=='*20)

metas = soup.select("meta[content='always']")
print(metas)