import os
import requests


def read_hero_file_csv():
    hero_file = open("./herofile/hero.csv", "r", encoding="utf-8")
    # hero_content=hero_file.read()
    lists = hero_file.readlines()

    # print(hero_content1)
    # print(hero_content)
    content = lists[1:]
    # print(content)
    lists1 = []
    for lists_element in content:
        # print(lists_element)
        hero_item = {}
        hero = lists_element[:-1]
        # print(hero)
        hero_list = hero.split(",")
        # print(hero_list)

        hero_item["hero_name"] = hero_list[0]
        hero_item["image_url"] = hero_list[1]
        # print(hero_list[1])
        # print(hero_item)
        lists1.append(hero_item)

    return lists1


def create_hero_dirs(hero_list):
    dir_before_name = "./herofile"
    for hero_element in hero_list:
        # print(hero_element)
        hero_name = hero_element["hero_name"]
        # print(hero_name)
        hero_path = dir_before_name + "/" + hero_name
        # print(hero_path)
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)
    print("所有项目以创建成功。")


def download_hero_image(hero_lists):
    dir_before_name = "./herofile"
    for hero_element in hero_lists:
        # print(hero_element)
        hero_name = hero_element["hero_name"]
        hero_url = hero_element["image_url"]
        # print(hero_name)
        # print(hero_url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
        response = requests.get(hero_url, headers=headers)
        image_content = response.content
        hero_path = dir_before_name + "/" + hero_name + "/" + "1" + hero_name + ".jpg"
        hero_file = open(hero_path, "wb")
        hero_file.write(image_content)
        hero_file.close()
        print("正在下载--（%s）--图片....." % hero_name)
    print("所有英雄图片已下载完成。")

    pass


def main():
    # 读取数据
    hero_datas = read_hero_file_csv()
    # print(hero_datas)
    create_hero_dirs(hero_datas)
    download_hero_image(hero_datas)
    pass


if __name__ == '__main__':
    main()
