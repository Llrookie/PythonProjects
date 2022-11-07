'''
    1、创建字典数据
        1.1 数据存储在excel中，可以在另一个py文件中读取数据，然后导入该模块
    2、导入ddt模块，帮我们实现数据驱动
    3、用ddt修饰，直接我们的unittest类
    4、用data修饰测试用例
    5。重写声明测试用例名称，test_ddt_1(self,para)
'''
import unittest
from selenium import webdriver
import time
from ddt import ddt,data

@ddt
class ddtTest2(unittest.TestCase):
    dataValue = [{'name': '792932348', 'pwd': 'RGNhai520marry1'}, {'name': '792932348', 'pwd': 'RGNhai520marry2'}]

    # 方法名不能改，self参数不能少
    def setUp(self):
       self.driver = webdriver.Chrome()
    def tearDown(self):
        pass

    @data(*dataValue)
    def test_ddt_1(self,para):

        # 1、打开腾讯首页：http: // www.qq.com
        self.driver.get('http://www.qq.com')
        time.sleep(3)
        # 2、点击邮箱图标
        self.driver.find_element_by_link_text('Qmail').click()
        # 3、跳转到QQ邮箱窗口，涉及到多窗口
        handlers = self.driver.window_handles
        self.driver.switch_to.window(handlers[1])
        # 验证窗口切换是否成功
        # driver.find_element_by_link_text('基本版').click()

        # 涉及到多表单处理，不然无法定位到对应元素
        # 方法一:默认是可以传frame的id或者name
        # driver.switch_to.frame("login_frame")
        # 方法二：可以传frame的元素对象
        iframeObject = self.driver.find_element_by_xpath('//*[@id="login_frame"]')
        self.driver.switch_to.frame(iframeObject)

        # 4、输入用户名
        self.driver.find_element_by_id('u').send_keys(para['name'])
        time.sleep(1)
        # 5、输入密码
        self.driver.find_element_by_id('p').send_keys(para['pwd'])
        time.sleep(1)
        # 6、点击登录
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        time.sleep(2)
        # 7、关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()