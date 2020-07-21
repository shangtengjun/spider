'''
需要输入验证码
1保存快照 2手动输入 3继续自动执行
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")

url = "https://www.douban.com/"

driver.get(url)
time.sleep(4)
driver.save_screenshot('yanzhengma.png')

driver.find_element_by_id('username').send_keys('15360631935')
driver.find_element_by_id('password').send_keys('Teng358.')

driver.find_element_by_name('btn btn-account btn-active').click()

time.sleep(4)

driver.save_screenshot('logined.png')

driver.quit()