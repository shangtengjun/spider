import requests
import lxml.html
import os


def parse_wangzhe_url(http_url):
    """抓取整个网站数据，返回页面数据"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    response = requests.get(http_url, headers=headers)
    html_content = response.content.decode("gbk")
    return html_content
    pass


def get_hero_datas(html_datas):
    """提取英雄信息，字段内容有英雄名称，英雄图片地址，详情链接地址等。。"""
    # 大空列表
    list = []
    metree = lxml.html.etree
    parser = metree.HTML(html_datas)
    li_list = parser.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    # print(li_list)
    # print(len(li_list))

    for li_element in li_list:
        # 空列表
        hero_item = []
        # 英雄名字
        hero_name = li_element.xpath("./a/text()")[0]
        # print(hero_name)
        hero_item.append(hero_name)
        # 图片地址
        image_url = "http:" + li_element.xpath("./a/img/@src")[0]
        # print(image_url)
        hero_item.append(image_url)
        # 获得详情链接地址
        detail_url = "https://pvp.qq.com/web201605/" + li_element.xpath("./a/@href")[0]
        # print(detail_url)
        hero_item.append(detail_url)
        # print(hero_item)
        list.append(hero_item)
        # print(list)
    return list

    pass


def save_hero_by_csv(hero_list1):
    """以csv格式保存数据内容"""
    dir_name="./herofile"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("目录%s以创建成功。"%dir_name)
        #创建文件

    hero_file=open(dir_name+"/hero.csv","w",encoding="utf-8")
        #表头
    hero_file.write("英雄名称，图片地址，详情地址\n")
        #print(hero_list1)
        #print(len(hero_list1))
    for element in hero_list1:
        hero=",".join(element)
            #print(hero)
        hero_file.write(hero+"\n")
            #写入数据
            #关闭文件
    hero_file.close()
    print("所有的英雄数据已保存成功.")


    pass


def main():
    """程序入口"""
    wangzhe_url = "https://pvp.qq.com/web201605/herolist.shtml"
    html_datas = parse_wangzhe_url(wangzhe_url)
    # print(html_datas)
    hero_list = get_hero_datas(html_datas)

    save_hero_by_csv(hero_list)
    pass


if __name__ == '__main__':
    main()
