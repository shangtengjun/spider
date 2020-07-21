import json
import random

def read_proxy_file():
    '''把保存的ip提取出来'''
    proxy_data = json.load(open("./ip_path/proxypool.json","r",encoding="utf-8"))
    return proxy_data
def get_proxy():
    '''随机提取一个ip'''
    proxy_datas = read_proxy_file()

    index = random.randint(0,len(proxy_datas)-1)
    return proxy_datas[index]

if __name__ == '__main__':
    print(get_proxy())