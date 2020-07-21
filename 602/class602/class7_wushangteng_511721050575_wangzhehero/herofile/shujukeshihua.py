import json
import os
from matplotlib import pyplot

def read_hero_data_from_json():
    """对hero_detail.json文件处理，获得英雄名称，皮肤个数"""
    hero_file=open("./herofile/hero_detail.json","r",encoding="utf-8")
    content=hero_file.read()
    #print(content)
    #print(type(content))
    hero_skin_list=json.loads(content)
    #名称列表
    hero_name_lists=[]
    #皮肤个数列表
    hero_skin_lists=[]

    for hero_element in hero_skin_list:
        #print(hero_element)
        heroe_name=hero_element["hero_name"]
        hero_name_lists.append(heroe_name)
        #皮肤个数
        skin_lengh=len(hero_element["hero_skins_list"])
        #print(heroe_name)
        #print(skin_lengh)
        hero_skin_lists.append(skin_lengh)
    return  hero_name_lists,hero_skin_lists

def draw_hero_image(x_tick,y):
    """绘制分析图"""
    #能正常显示中文
    pyplot.rcParams["font.sans-serif"]=["SimHei"]
    #0-93数字
    x=[i for i in range(1,len(x_tick)+1)]
    #print(x)
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
    hero_name_datas,skin_lengh_datas=read_hero_data_from_json()
    draw_hero_image(hero_name_datas,skin_lengh_datas)

if __name__ == '__main__':
    main()