#导包
# from selenium import webdriver
#页面元素定位及操作
#使用id定位
#导包
# from selenium import webdriver
# import time
# #获取驱动
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# #通过id定位元素并操作
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# #打开页面等待两秒
# time.sleep(2)
# #退出浏览器
# driver.quit()

#使用name属性定位
# from selenium import webdriver
# import time
# #获取驱动
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# #通过id定位元素并操作
# driver.find_element_by_class_name('s_ipt').send_keys('selenium')
# driver.find_element_by_class_name('s_btn').click()
# #打开页面等待两秒
# time.sleep(2)
# #退出浏览器
# driver.quit()

from selenium import webdriver
import time
#获取驱动
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)
#通过link text定位元素并操作
#driver.find_element_by_link_text('新闻').click()
#通过partial link text定位元素，部分匹配
driver.find_element_by_partial_link_text('hao').click()
#打开页面等待两秒
time.sleep(3)
#退出浏览器
driver.quit()