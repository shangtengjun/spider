import pandas
from matplotlib import pyplot
import numpy

def read_offer_data_excel():
    """从 Excel 表格中获取数据内容"""
    data_results = pandas.read_excel("./lastoffer/招聘 Python 岗位信息表.xls")
    #print("所有数据内容:",data_results)
    #print("类型:",type(data_results))
    # 矩阵! --线性代数
    #print("-----------------------------------")
    #offers = data_results["职位名"]
    #print(offers)
    #print(type(offers))
    #print("-----------------------------------")
    salary_values = data_results["薪资"]
    return salary_values



def main():

    offer_salarys = read_offer_data_excel()
    count_5k = 0
    count_9k = 0
    count_14k = 0
    count_master = 0
    #下标值
    index = 0
    while index < offer_salarys.size:
        if offer_salarys[index]<5000:
            count_5k += 1
        elif offer_salarys[index]<9000:
            count_9k += 1
        elif offer_salarys[index]<14000:
            count_14k += 1
        else:
            count_master += 1
        index += 1
    # 绘制分布图
    pyplot.rcParams["font.sans-serif"]=["SimHei"]
    data=[count_5k,count_9k,count_14k,count_master]
    labels = ["五千以下","5-9k","9-14k","14k以上"]
    explores = [0,0,0,0.05]
    pyplot.pie(data,labels=labels,autopct="%2.2f%%",explode=explores)
    # 标题
    pyplot.title("Python 岗位薪资占比分布")
    pyplot.legend(loc="upper left")
    pyplot.show()


if __name__ == '__main__':
    main()