from selenium import webdriver
driver=webdriver.Chrome("E:\\第一周\\04第4天-王者荣耀皮肤爬虫(二)\\4.软件工具\\Chrome浏览器\\chrome驱动文件\\chromedriver.exe")
driver.get("http://www.baidu.com")
html_content=driver.page_source
print(html_content)
driver.quit()