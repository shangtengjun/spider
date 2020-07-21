from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")

url = 'http://www.baidu.com/'

driver.get(url)

text = driver.find_element_by_id('wrapper').text

print(text)
print(driver.title)

#得到界面的截图快照
driver.save_screenshot('index.png')

#id='kw'是百度的输入框，得到这个元素ui后直接输入内容‘大熊猫’
driver.find_element_by_id('kw').send_keys(u'大熊猫')

#id=‘su’是搜索按钮，click模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot('daxiongmao.png')

#获取当前页面的cookie
print(driver.get_cookies())

#模拟两个按键 ctal a 全选 x 剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

driver.find_element_by_id('kw').send_keys(u'美女')
driver.save_screenshot('meinv.png')

driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('meinv2.png')

#清空输入框
driver.find_element_by_id('kw').clear()
time.sleep(5)
driver.save_screenshot('clear.png')

#关闭浏览器
driver.quit()
