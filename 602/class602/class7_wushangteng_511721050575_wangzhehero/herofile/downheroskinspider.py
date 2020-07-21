import  json
import requests
def read_hero_json():

    #dirl_before_name="./herofile"
    hero_skin_file=open("./herofile/hero_detail.json",'r',encoding="utf-8")
    #print(hero_file)
    content=hero_skin_file.read()
    #print(content)
    #prin t(type(content))
    #转换py类型数据
    py_hero_skin=json.loads(content)
    hero_skin_file.close()
    return  py_hero_skin


def main():
    hero_skin_datas=read_hero_json()
    for element in hero_skin_datas:
        #print(element)
        hero_name=element["hero_name"]
        hero_skin_lists=element["hero_skins_list"]
        for skin_element in hero_skin_lists:
            #print(skin_element)
            skin_name=skin_element["skin_name"]
            skin_url=skin_element["skin_url"]

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
            response=requests.get(skin_url,headers=headers)
            image_content=response.content  #图片内容

            image_file=open("./herofile/"+hero_name+"/"+skin_name+".jpg","wb")
            image_file.write(image_content)
            image_file.close()
            print("正在下载（%s）--皮肤（%s)图片..."%(hero_name,skin_name))
        print("..............%s的所有皮肤下载完毕"%hero_name)
    print("所有英雄皮肤下载完成")


if __name__ == '__main__':
    main()