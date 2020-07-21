import requests
import time

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 第一次 lasthotcommentid 为空
lasthotcommentid = ''
# 前五页
for pagenum in range(5):
  params = {
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '212877900',
    'cmd': '8',
    'needmusiccrit': '0',
    'pagenum': pagenum,
    'pagesize': '20',
    'lasthotcommentid': lasthotcommentid,
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010'
  }
  res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg', headers=headers, params=params)
  data = res.json()
  for item in data['comment']['commentlist']:
    print('{}：{}'.format(item['nick'], item['rootcommentcontent']))
  # 当前页最后一个评论的 commentid 作为下一页的 lasthotcommentid
  lasthotcommentid = data['comment']['commentlist'][-1]['commentid']
  # 防止爬取太快被封
  time.sleep(1)