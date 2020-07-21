import requests
import json
class WeiboSpider():
  def __init__(self, username, password):
    self.session = requests.Session()
    self.headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
      'referer': 'https://passport.weibo.cn/signin/login'
    }
    self.session.headers.update(self.headers)
    self.username = username
    self.password = password

  def login(self):
    login_data = {
      'username':  self.username,
      'password':  self.password,
      'savestate': '1',
      'r': 'https://m.weibo.cn/?jumpfrom=weibocom',
      'ec': '0',
      'pagerefer': 'https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F%253Fjumpfrom%253Dweibocom',
      'entry': 'mweibo',
      'wentry': '',
      'loginfrom': '',
      'client_id': '',
      'code': '',
      'qq': '',
      'mainpageflag': '1',
      'hff': '',
      'hfp': ''
    }

    self.session.post('https://passport.weibo.cn/sso/login', data=login_data)

  def get_st(self):
    config_req = self.session.get('https://m.weibo.cn/api/config')
    #config = config_req.json()
    config = json.loads(config_req.content.decode (encoding='utf8'))

    st = config['data']['st']

    return st

  def compose(self, content):

    compose_data = {
      'content': content,
      'st': self.get_st()
    }

    compose_req = self.session.post('https://m.weibo.cn/api/statuses/update', data=compose_data)
    print(compose_req.json())

  def send(self, content):
    self.login()
    self.compose(content)

weibo = WeiboSpider('13192862027', 'teng358.')
weibo.login()


weibo.send('本条微博由 Python 发送')