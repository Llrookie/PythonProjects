from selenium import webdriver
import time

#driver = webdriver.Chrome()
#打开页面
#driver.get("https://www.baidu.com")

# #设置窗口大小
# driver.set_window_size(1920,600)
# time.sleep(3)
# #设置为最大窗口
# driver.maximize_window()
# time.sleep(3)
# #设置为最小窗口
# driver.minimize_window()
# time.sleep(3)

#页面的前进和后退
#打开新闻页面
# driver.find_element_by_link_text('新闻').click()
# time.sleep(2)
# #后退到百度页面
# driver.back()
# time.sleep(3)
# #前进到新闻页面
# driver.forward()
#
# #执行下刷新操作
# driver.refresh()

#截图操作
#driver.save_screenshot(r"D:\a.png")

# driver.quit()
'''
    set_window_size(1920,600):设置窗口大小
    maximize_window():设置为最大窗口
    minimize_window():设置为最小窗口
    driver.back():控制页面后退
    driver.forward():控制页面前进
    driver.refresh():刷新页面
    save_screenshot(r"D:\a.png"):保存截图
    quit():关闭所有窗口
    close():关闭当前窗口
'''
#切换窗口
# driver = webdriver.Chrome()
# driver.get('https://www.taobao.com')
# handler1 = driver.current_window_handle
# handlers = driver.window_handles
# # driver.switch_to_window(handler name)
# print(handler1)

