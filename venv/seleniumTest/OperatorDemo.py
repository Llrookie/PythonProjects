from selenium import  webdriver
import time

'''
    clear():清除文本
    send_keys():模拟键盘输入
    click():点击元素
    current_url:返回当前页面的url地址，可用于断言
    title:获取当前页面的title
    Text():获取页面显示的文本(提示框、警告框)
    get_attribute(name):获取属性值，
    is_displayed():设置该属性是否用户可见,结果值为布尔值
    
'''

driver = webdriver.Chrome()
#打开页面
driver.get("https://www.baidu.com")
#获取文本并打印
tt = driver.find_element_by_xpath('//*[@id="lm-new"]/div/a').text
print(tt)
value1 = driver.find_element_by_id('kw').get_attribute('class')
print(value1)   #wd
#判断该属性是否可见
boo = driver.find_element_by_id('su').is_displayed()
print(boo)
#判断该属性是否可用
boo1 = driver.find_element_by_id('su').is_enabled()
print(boo1)

driver.quit()