from PIL import Image
import pytesseract
import requests

url = "http://www.cnxhyp.com/api/image.png.php?auth=8e59p7CdwkARbg9ckaSIZnCmcsmvFULBV1JKM3BJKqD8xqbcDfWwafFQ5w"

headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'http://www.cnxhyp.com/sell/show-2702.html'

    }
req = requests.get(url,headers=headers)

rsp = req.content

f = open("./tupian.png",'wb')
f.write(rsp)
f.close()
image = Image.open('./tupian.png')
content = pytesseract.image_to_string(image)   # 解析图片
print(content)