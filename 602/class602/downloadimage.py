# coding:utf-8
"""
思路分析：
    （1）发送请求，获得图片的内容；  --requests
    （2）把图片内容写入到一个文件中。  --文件操作
"""
import requests

# 发送请求，获得图片的内容
image_url = "http://www.xiaohuar.com/d/file/20190227/257e9f91df2bbd45c537f9416ae3afbb.jpg"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response = requests.get(image_url, headers=headers)
# 图片的内容
image_content = response.content

# 把图片内容写入到一个文件中
writer = open("./image/girl.jpg", "wb")
writer.write(image_content)
writer.close()
print("下载一张图片成功!")
