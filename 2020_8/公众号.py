import requests
import json
import urllib3
import time
urllib3.disable_warnings()
# 请求地址
url = 'https://mp.weixin.qq.com/mp/profile_ext?'
# 添加请求头
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
# 请求参数
for i in range(0,5):
    print('开始抓取第%s页数据'%(i+1))
    params={
      '__biz': 'MjM5NDAwMTA2MA==',
            'uin': 'MTczODIyNzg3Nw==',
            'key': 'f0a7c0779e79e92b25b1a3f8779ec559b50f247ff4dd1ece070c17dd08d9dbdc602bbd8c5837e4b68c252507ac45796c2f928b87d1cdfdbd2852c1b48f9e019806524a1c8d633b8886c30d48f6a82a8c',
            'offset': (i*10)+122,
            'count': (i*10)+10,
            'action': 'getmsg',
            'f': 'json'
    }
    # 获取请求的json格式
    r = requests.get(url,headers=headers,params=params,verify = False).json()
    msg_list = json.loads(r['general_msg_list'])
    list = msg_list.get('list')
    for i in list:
        info_list = i['app_msg_ext_info']
        # 获取标题
        title = info_list['title']
        print(title)
        # 链接
        content_url = info_list['content_url']
        print(content_url)
        #发布时间
        datetime_list = i['comm_msg_info']['datetime']
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime_list))
        print(datetime)