import json
import requests
import useragentutil

def get_proxy_fromjson ( ):
    '''从文件中拿出ip'''
    proxy_file = open("./ip_path/proxydata.json", "r", encoding="utf-8")
    proxys = proxy_file.read()
    proxy_id = json.loads(proxys)
    proxy_file.close()
    return proxy_id

def main():
    '''对IP进行处理，好留坏丢'''
    proxy_ip_datas = get_proxy_fromjson()
    url = "https://www.sohu.com/"
    value_proxy_list = []
    for proxy in proxy_ip_datas:
        try:
            proxy_response = requests.get(url,headers=useragentutil.get_headers(),proxies=proxy)
            if proxy_response.status_code == 200:
                value_proxy_list.append(proxy)
                #with open("./ip_path/proxypool.json","w",encoding="utf-8") as file
                json.dump(value_proxy_list,
                          open("./ip_path/proxypool.json","w",encoding="utf-8"),
                          ensure_ascii=False,
                          indent=2)
                print("正在处理ip：{}".format(proxy))
        except Exception:
            print("异常ip：{}".format(proxy))



if __name__ == '__main__':
    main()
