'''手动使用cookie'''

from urllib import request

if __name__ == '__main__':
    url = 'http://www.renren.com/972226789/profile'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        #cookie使http有记忆性，若不使用则无法访问登录界面
        "Cookie" : "anonymid=k0g46lvf-myffq; depovince=GUZ; _r01_=1; JSESSIONID=abcHsBS2HBFWY4TGNCJ0w; ick_login=32e253de-19fe-4999-a00b-0258873cf249; t=2f796ac8bad71623051662f175493f649; societyguester=2f796ac8bad71623051662f175493f649; id=972226789; xnsid=dc8d01b2; jebecookies=8500726e-363d-4791-8e7f-235151cd3ad4|||||; ver=7.0; loginfrom=null; jebe_key=b8b390a7-5c97-4156-9d3e-5a379781d514%7C3a476ea6cbdb499a5b791215df06c845%7C1568257814004%7C1%7C1568257815561; jebe_key=b8b390a7-5c97-4156-9d3e-5a379781d514%7C3a476ea6cbdb499a5b791215df06c845%7C1568257814004%7C1%7C1568257815564; wp_fold=0"

    }

    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open('rsp2.html','w',encoding='utf-8') as f:
        f.write(html)