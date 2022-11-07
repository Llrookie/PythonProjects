''''
  多表单(一个窗口中)：
    在一个页面嵌套另外一个页面，如frame/iframe;现在很多web页面使用的一种方式。webdriver对象只能在一个页面中定位元素，需要一种方式将driver对象
    从外层切换给内层使用，才能对内层的元素进行操作

    driver.switch_to.frame()

    案例：
        1、打开腾讯首页：http://www.qq.com
        2、点击邮箱图标
        3、输入用户名
        4、输入密码
        5、点击登录
        6、关闭浏览器
'''
from selenium import webdriver
import time

# 1、打开腾讯首页：http: // www.qq.com
driver = webdriver.Chrome()
driver.get('http://www.qq.com')
driver.implicitly_wait()
# 2、点击邮箱图标
driver.find_element_by_link_text('Qmail').click()
#3、跳转到QQ邮箱窗口，涉及到多窗口
handlers = driver.window_handles
driver.switch_to.window(handlers[1])
#验证窗口切换是否成功
# driver.find_element_by_link_text('基本版').click()

#涉及到多表单处理，不然无法定位到对应元素
#方法一:默认是可以传frame的id或者name
# driver.switch_to.frame("login_frame")
#方法二：可以传frame的元素对象
iframeObject = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(iframeObject)

# 4、输入用户名
driver.find_element_by_id('u').send_keys('792932348')
time.sleep(1)
# 5、输入密码
driver.find_element_by_id('p').send_keys('RGNhai520marry1')
time.sleep(1)
# 6、点击登录
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(1)
# 7、关闭浏览器
driver.quit()
