'''模拟自动登录'''
# 从 selenium 中导入 webdriver（驱动）
from selenium import webdriver

# 选择 Chrome 浏览器并打开
browser = webdriver.Chrome()



# 打开博客
browser.get('https://wpblog.x0y1.com')
# 找到登录按钮
login_btn = browser.find_element_by_link_text('登录')
# 点击登录按钮
login_btn.click()
# 找到用户名输入框
user_login = browser.find_element_by_id('user_login')
# 输入用户名
user_login.send_keys('codetime')
# 找到密码输入框
user_pass = browser.find_element_by_id('user_pass')
# 输入密码
user_pass.send_keys('shanbay520')
# 找到登录按钮
wp_submit = browser.find_element_by_id('wp-submit')
# 点击登录按钮
wp_submit.click()
# 找到第一篇文章
more_link = browser.find_element_by_class_name('more-link')
# 点击第一篇文章
more_link.click()
# 找到评论框
comment = browser.find_element_by_id('comment')
# 输入评论
comment.send_keys('由 selenium 自动评论')
# 找到发表评论按钮
submit = browser.find_element_by_id('submit')
# 点击发表评论按钮
submit.click()
# 关闭浏览器
browser.quit()