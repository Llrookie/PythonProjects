#Xpath定位
'''
    绝对路径：/
    相对路径：//

'''
# from selenium import webdriver
# import  time
#
# driver = webdriver.Chrome()
# driver.get('https://baidu.com')
# driver.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('selenium')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# #/html/body/div/div[2]/div[5]/div[1]/div/form/span[2]/input
# time.sleep(3)
#
# driver.quit()

'''
    css定位方法
'''
from selenium import webdriver
import  time

driver = webdriver.Chrome()
driver.get('https://baidu.com')
driver.find_element_by_css_selector('.s_ipt').send_keys('selenium')
driver.find_element_by_css_selector('#su').click()
time.sleep(3)

driver.quit()
'''
    .表示类选择器，eg:.s_ipt
    #表示id选择器，eg:#kw,#su
    >表示父子关系，eg:span > input
'''



