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
    # 绘制薪资分布图
    pyplot.figure(figsize=(18,8),dpi=80)

    # 标题
    pyplot.title ("python岗位工资分析表")
    # x/y
    pyplot.xlabel ("个数")
    pyplot.ylabel ("工资")
    # 处理中文乱码
    pyplot.rcParams["font.sans-serif"]=["SimHei"]
    #x 轴 (x,y) --y
    x = [i for i in range(1,offer_salarys.size+1)]
    # 绘制
    pyplot.scatter(x,offer_salarys,label="薪资")
    #x刻度
    x_tick = [i for i in range(0,offer_salarys.size+1,30)]
    pyplot.xticks(x_tick,x_tick,rotation=45)
    #y刻度
    y_tick = [i for i in range(0,45000,2000)]
    pyplot.yticks(y_tick)
    #最值
    pyplot.xlim(0,1002)
    pyplot.ylim(0,41000)
    #网格
    pyplot.grid(alpha=0.5)
    # 绘制均值线
    average=numpy.mean(offer_salarys)
    #print("平均薪资:",average)
    # 处理
    avg_list=[average for i in x]
    #print(avg_list)
    pyplot.plot(x,avg_list,"r",linewidth=3,label="平均薪资")
    # 绘制均值数值
    pyplot.text(0,average+200,"均薪:"+str(average),color="red")
    # 绘制图例
    pyplot.legend(loc=0)
    #显示
    pyplot.show()


if __name__ == '__main__':
    main()