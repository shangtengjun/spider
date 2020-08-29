import  urllib.request
import  useragentutil
import lxml.html
import os
import json

def parse_proxy_url(temp_url):
    '''爬取请求解析网站，获取网页源码'''
    request = urllib.request.Request(temp_url,headers=useragentutil.get_headers())
    #发送请求，获得结果
    rsp = urllib.request.urlopen(request).read().decode()
    return  rsp


def catch_proxy_value_list(html_content):
    """提取数据内容"""
    # 定义变量
    proxy_lists = []
    # （1）解析器对象； --用于解析html代码
    metree = lxml.html.etree
    proxy_parser = metree.HTML(html_content)
    # （2）获得所有的tr列表；
    tr_list = proxy_parser.xpath("//table[@id='ip_list']/tr")[1:]

    # （3）遍历tr列表，tr单个元素；
    for tr_element in tr_list:
        # IP代理值
        ip_item = {}
        # （4）提取数据内容；
        # IP地址、端口、类型
        ip = tr_element.xpath("./td[2]/text()")[0]
        duankou = tr_element.xpath("./td[3]/text()")[0]
        # print(ip)   # 列表,获取里面的元素
        agreement = tr_element.xpath("./td[6]/text()")[0]  # HTTP

        ip_item[agreement] = agreement.lower()+"://"+ip+":"+duankou
        proxy_lists.append(ip_item)

    return proxy_lists

def save_proxy_file(datas):
    """保存所有的IP代理数据到json文件中"""
    # 保存文件
    ip_path = "./ip_path"
    if not os.path.exists(ip_path):
        os.makedirs(ip_path)
    json.dump(datas,
              open(ip_path+"/proxypool.json","w",encoding="utf-8"),
              ensure_ascii=False,
              indent=2)
    print("所有IP数据已保存成功")


def main():
    proxy_url = "https://www.xicidaili.com/nn/2"

    html = parse_proxy_url(proxy_url)

    data = catch_proxy_value_list(html)

    save_proxy_file(data)


if __name__ == '__main__':
    main()
