# coding:utf-8
"""
思路分析：
（1）爬取整个新浪网的页面数据内容；
（2）把爬取下来的数据内容保存到一个文件中。
"""
import requests
import useragentutil

sina_url = "https://www.sina.com.cn/"
# 爬取整个新浪网的页面数据内容
headers = useragentutil.get_headers()
# print(headers)
response = requests.get(sina_url, headers=headers)
# 获得内容
# html_content = response.text
html_content = response.content.decode("utf-8")
# print(html_content)

# 把爬取下来的数据内容保存到一个文件中
writer = open("./file/sina.html", "w",encoding="utf-8")
writer.write(html_content)
writer.close()
print("新浪网页面数据已保存成功!")
