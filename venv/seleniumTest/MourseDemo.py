from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(3)
#控制鼠标悬浮到“设置”按钮上
setbutton = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
#将对“设置”按钮的操作行为封装到ActionChains，到这一步，鼠标对象已经知道要干啥了，还没开始
ActionChains(driver).move_to_element(setbutton).perform()
ActionChains(driver).drag_and_drop()
time.sleep(5)
driver.quit()

'''
鼠标操作：
    move_to_element():鼠标悬停
    context_click():右击
    double_click():双击
    drag_and_drop():拖动
'''