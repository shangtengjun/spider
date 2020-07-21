import requests
import lxml.html #页面解析
import os #操作文件
from selenium import webdriver
import json
from matplotlib import pyplot


def parse_wangzhe_url(http_url):
    '''抓取整个网站数据，返回页面数据'''

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    response = requests.get(http_url, headers=headers)
    html_content = response.content
    return html_content
# 大空列表，装英雄信息
lists = []
def get_hero_datas(html_content):
    '''提取英雄信息，字段内容有英雄名称，英雄图片地址，详情链接地址等。。'''
    metree = lxml.html.etree
    parser = metree.HTML(html_content)
    li_list = parser.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    # print(li_list)
    i = 0
    for li_element in li_list:

        hero_item = []
        # 英雄名字
        hero_name = li_element.xpath("./a/text()")[0]
        hero_item.append(hero_name)
        # 图片地址
        image_url = "https:"+li_element.xpath("./a/img/@src")[0]

        hero_item.append(image_url)
        # 获得详情链接地址
        detail_url = "https://pvp.qq.com/web201605/"+li_element.xpath("./a/@href")[0]
        hero_item.append(detail_url)
        lists.append(hero_item)
    return lists


def save_hero_datas_by_csv(hero_lists):
    '''以csv格式保存数据内容'''
    dir_name = "./herofile"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    hero_file = open(dir_name + "/hero.csv", "w", encoding="utf-8")
    hero_file.write("英雄名称,图片地址,详情地址\n")
    for element in hero_lists:
        hero = ",".join(element)
        hero_file.write(hero + "\n")
    hero_file.close()


def read_hero_file_from_csv():
    #提取名字和头像
    hero_file = open("./herofile/hero.csv",'r',encoding="utf-8")
    lines = hero_file.readlines()
    content = lines[1:]
    lists2 = []
    for hero_element in content:
        hero_item = {}
        hero = hero_element[:-1]
        hero_list = hero.split(',')
        hero_item['hero_name'] = hero_list[0]
        hero_item['image_url'] = hero_list[1]
        lists2.append(hero_item)
    return lists2


def create_hero_dirs(hero_list):
    for hero_element in hero_list:
        hero_name = hero_element['hero_name']
        hero_path = "./herofile/"+hero_name
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)


def download_hero_image(hero_list):
    for hero_element in hero_list:
        hero_name = hero_element['hero_name']
        image_url = hero_element['image_url']
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

        response = requests.get(image_url, headers=headers)
        image_content = response.content
        hero_path = "./herofile/"+hero_name+'/1'+hero_name+'.jpg'
        hero_file = open(hero_path,'wb')
        hero_file.write(image_content)
        hero_file.close()
        print('正在下载--(%s)--'%hero_name)


def read_hero_file_from_csv2():
    '''通过读取csv文件数据,提取英雄名称.详情地址。。'''
    hero_file = open("./herofile/hero.csv", 'r',encoding="utf-8")
    lines = hero_file.readlines()
    content = lines[1:]
    lists3 = []
    for hero_element in content:
        hero_item = {}
        hero = hero_element
        hero_list = hero.split(',')
        hero_item['hero_name'] = hero_list[0]
        hero_item['image_detail_url'] = hero_list[2]
        lists3.append(hero_item)
    return lists3


def parse_hero_detail_url(wang_url):
    '''获取页面数据'''
    driver = webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")
    driver.get(wang_url)
    html_content = driver.page_source
    #print(html_content)
    driver.quit()
    return html_content


def get_hero_skin_datas(html_content):
    metree = lxml.html.etree
    parser = metree.HTML(html_content)
    li_list = parser.xpath("//div[@class='pic-pf']/ul[@class='pic-pf-listpic-pf-list3']/li")
    lists = []
    for li_element in li_list:
        skin_item = {}
        skin_name = li_element.xpath("./p/text()")[0]
        skin_item["skin_name"] = skin_name
        skin_url = "http:" + li_element.xpath("./i/img/@data-imgname")[0]
        skin_item["skin_url"] = skin_url
        lists.append(skin_item)
    return lists


def save_hero_skin_data_by_json(hero_lists):
    '''以json格式的文件保存数据内容'''
    json_strs = json.dumps(hero_lists, ensure_ascii=False, indent=2)
    hero_file = open("./herofile/hero_detail.json", "w",encoding="utf-8")
    hero_file.write(json_strs)
    hero_file.close()


def read_hero_skin_from_json():
    """读取 hero_detail.json 文件中的数据； --名称、皮肤地址"""
    hero_skin_file = open("./herofile/hero_detail.json", "r",encoding="utf-8")
    content = hero_skin_file.read()
    py_hero_skins = json.loads(content)
    hero_skin_file.close()
    return py_hero_skins

def read_hero_data_from_json():
    """对hero_detail.json文件处理，获得英雄名称，皮肤个数"""
    hero_file=open("./herofile/hero_detail.json","r",encoding="utf-8")
    content=hero_file.read()
    hero_skin_list=json.loads(content)
    #名称列表
    hero_name_lists=[]
    #皮肤个数列表
    hero_skin_lists=[]

    for hero_element in hero_skin_list:

        heroe_name=hero_element["hero_name"]
        hero_name_lists.append(heroe_name)
        #皮肤个数
        skin_lengh=len(hero_element["hero_skins_list"])

        hero_skin_lists.append(skin_lengh)
    return  hero_name_lists,hero_skin_lists


def draw_hero_image(x_tick,y):
    """绘制分析图"""
    #能正常显示中文
    pyplot.rcParams["font.sans-serif"]=["SimHei"]
    #0-93数字
    x=[i for i in range(1,len(x_tick)+1)]

    #画布大小
    pyplot.figure(figsize=(24,10),dpi=80)
    #绘制网格
    pyplot.grid(alpha=0.4)
    #添加标题
    pyplot.title("王者荣耀皮肤个数数据分析图")
    #纵横坐标标题
    pyplot.xlabel("英雄名称")
    pyplot.ylabel("皮肤个数（单位:个）")
    #条形图
    pyplot.bar(x,y,width=0.8)
    #设置x轴的最小最大值
    pyplot.xlim(0,len(x_tick)+1)
    #调整x刻度----显示中文有误
    pyplot.xticks(x,x_tick,rotation=75)
    #保存图片
    dir_name="./image"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    #保存
    pyplot.savefig(dir_name+"/hero.png")
    #显示图形
    pyplot.show()


def main():
    '''程序入口"'''
    wangzhe_url = "https://pvp.qq.com/web201605/herolist.shtml"
    html_datas = parse_wangzhe_url(wangzhe_url)

    html_herodatas = get_hero_datas(html_datas)

    save_hero_datas_by_csv(html_herodatas)
    hero_lists = read_hero_file_from_csv()
    create_hero_dirs(hero_lists)
    download_hero_image(hero_lists)

    hero_datas = read_hero_file_from_csv2()
    all_hero_skin_lists = []



    for element in hero_datas:
        item = {}
        hero_name = element["hero_name"]
        item["hero_name"] = hero_name
        detail_url = element["image_detail_url"]
        html_datas = parse_hero_detail_url(detail_url)
        item["hero_skins_list"] = get_hero_skin_datas(html_datas)
        all_hero_skin_lists.append(item)




    save_hero_skin_data_by_json(all_hero_skin_lists)

    hero_skin_datas = read_hero_skin_from_json()

    for element in hero_skin_datas:
        hero_name = element["hero_name"]
        hero_skin_lists = element["hero_skins_list"]

        for skin_element in hero_skin_lists:
            skin_name = skin_element["skin_name"]
            skin_url = skin_element["skin_url"]
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
            response = requests.get(skin_url, headers=headers)
            image_content = response.content
            image_file = open("./herofile/" + hero_name + "/" + skin_name + ".jpg", "wb")
            image_file.write(image_content)
            image_file.close()
            print("正在下载(%s)-->皮肤[%s]图片..." % (hero_name, skin_name))

    print("所有英雄皮肤均已下载完成!")

    hero_name_datas, skin_lengh_datas = read_hero_data_from_json()
    draw_hero_image(hero_name_datas, skin_lengh_datas)


if __name__ == '__main__':
    main()