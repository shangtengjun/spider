from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content,'lxml')
print(soup)

#bs自动解码
content = soup.prettify()

#print(content)

print('=='*20)
print(soup.link)
print(soup.link.name)
print(soup.link.string)

print('=='*20)
print(soup.title)
print(soup.title.attrs)
print('=='*20)
print(soup.attrs)