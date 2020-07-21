from selenium import webdriver
import lxml.html
import json


def read_hero_data_csv():
    """通过读取csv文件数据,提取英雄名称.详情地址。。"""
    dir_before_name="./herofile"
    hero_file=open(dir_before_name+"/hero.csv","r",encoding="utf-8")
    lists=hero_file.readlines()[1:]
    #print(lists)
    lists1=[]
    for element in lists:
        item={}
        #print(element[:-1])
        hero=element[:-1]
        hero_list=hero.split(",")
        #print(hero_list)
        hero_name=hero_list[0]
        item["hero_name"]=hero_name
        #详情地址
        hero_detail_url=hero_list[2]
        #print(hero_detail_url)
        item["hero_detail_url"]=hero_detail_url
        #print(hero_name)
        #print(hero_detail_url)
        #print(item)
        lists1.append(item)
    return  lists1

def parse_hero_detail_url(http_url):
    """获取页面数据"""
    #操作浏览器
    
    driver=webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")

    #放大窗口
    driver.maximize_window()
    #请求网址
    driver.get(http_url)

    #获取网页数据内容
    html_content=driver.page_source
    #print(html_content)
    #关闭浏览器
    driver.quit()
    return html_content


def get_hero_skin_datas(html_content):
    metree=lxml.html.etree
    parser=metree.HTML(html_content)
    #解析页面
    li_list=parser.xpath("//div[@class='pic-pf']/ul[@class='pic-pf-list pic-pf-list3']/li")
    #print(li_list)
    #print(len(li_list))
    lists=[]

    for li_element in li_list:
        skin_item={}
        #皮肤名称
        skin_name=li_element.xpath("./p/text()")[0]
        #print(skin_name)
        skin_item["skin_name"]=skin_name
        #皮肤地址
        skin_url="http:"+li_element.xpath("./i/img/@data-imgname")[0]
        #print(skin_url)
        skin_item["skin_url"]=skin_url
        lists.append(skin_item)
    return  lists

    pass


def save_hero_skin_data_by_json(hero_lists):
    """以json格式的文件保存数据内容"""
    json_strs=json.dumps(hero_lists,ensure_ascii=False,indent=2)

    hero_file=open("./herofile/hero_detail.json","w",encoding="utf-8")
    hero_file.write(json_strs)
    hero_file.close()
    print("数据保存完成")
    pass


def main():
    hero_datas=read_hero_data_csv()
    #print(hero_datas)
    #parse_hero_detail_url(hero_datas)

    all_hero_skin_lists=[]
    for element in hero_datas:
        item={}
        #print(element)
        hero_name=element["hero_name"]
        item["hero_name"]=hero_name
        #详情地址
        detail_url=element["hero_detail_url"]
        #print(hero_name)
        #获取皮肤的页面数据内容
        html_datas=parse_hero_detail_url(detail_url)
        #print(html_datas)
        item["hero_skins_list"]=get_hero_skin_datas(html_datas)
        print(item)
        #添加到大列表
        all_hero_skin_lists.append(item)
    print(all_hero_skin_lists)
    save_hero_skin_data_by_json(all_hero_skin_lists)





if __name__ == '__main__':
    main()