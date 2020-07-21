'''登录后利用cookie发表评论'''
import requests

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 登录参数
login_data = {
  'log': 'codetime',
  'pwd': 'shanbay520',
  'wp-submit': '登录',
  'redirect_to': 'https://wpblog.x0y1.com',
  'testcookie': '1'
}
# 评论参数
comment_data = {
  'comment': '由 Python 自动评论',
  'submit': '发表评论',
  'comment_post_ID': '34',
  'comment_parent': '0'
}
#session 相当于在服务器上建立的一份用户档案，cookie 中只要存储用户的身份信息，服务器通过身份信息在 session 中查询用户的其他信息。
session = requests.Session()

#通过 session.headers.update() 方法来更新全局的 headers，通过该 session 发送的请求都会使用我们设置的全局 headers。
session.headers.update(headers)

# 使用 session 登录
login_req = session.post('https://wpblog.x0y1.com/wp-login.php', data=login_data)
# 使用 session 发评论
comment_req = session.post('https://wpblog.x0y1.com/wp-comments-post.php', data=comment_data)
# 状态码为 200 表示评论成功
print(comment_req.status_code)