from urllib import request,parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"

    wd = input("Input your keyword:")
    #想要使用data，需要使用字典结构
    qs = {
        'wd':wd
    }
    #转换url编码,返回str类型
    qs = parse.urlencode(qs)

    fullurl = url + qs

    print(fullurl)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    rsp = request.Request(url=fullurl, headers=headers)

    html = request.urlopen(rsp).read().decode()

    print(html)