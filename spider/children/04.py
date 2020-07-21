'''error使用'''

from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    try:
        req = request.Request(url=url,headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError:{}'.format(e.reason))
        print(e)

    except error.URLError as e:
        print('URLError:{}'.format(e.reason))
        print(e)

    except Exception as e:
        print(e)