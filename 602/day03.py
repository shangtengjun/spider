'''
user1 = ['s01','花木兰','24','广东韶关']
user2 = ['s02','宫本','22','广东广州']
user3 = ['s03','诸葛亮','21','广东普宁']
users = [user1,user2,user3]

writer = open('./class602/class/student.csv','w',encoding='gbk')

for temp in users:
    element = ','.join(temp)

    writer.write(element+'\n')
writer.close()
'''
'''
import requests
import lxml.html as lh

http_url = 'https://www.baidu.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response = requests.get(http_url, headers=headers)
html_content = response.content.decode('utf-8')

metree = lh.etree
parser = metree.HTML(html_content)
logo_url = 'http:'+parser.xpath("//div[@id='lg']/img[@class='index-logo-src']/@src")[0]
print(logo_url)

a_list = parser.xpath("//div[@id='u1']/a")
for a_element in a_list:
    content = a_element.xpath("./text()")[0]
    print(content)
    href_url = a_element.xpath("./@href")[0]
    print(href_url)
'''

import  requests
import  lxml.html

http_url = 'http://www.hualixy.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response = requests.get(http_url, headers=headers)
html_content = response.content.decode('utf-8')

metree = lxml.html.etree
parser = metree.HTML(html_content)
message = parser.xpath("//div[@id='wp_news_w8']/ul/li")[0]

for mess in message:
    mess_li = mess.xpath("./div")[0]
    print(mess_li)


