from interface_class.api_key.key_test import Apidemo
import unittest
from ddt import ddt,file_data

@ddt
# ddt读取yaml文件数据
class CaseDemo(unittest.TestCase):
    # 前置方法，将Apidemo类实例化
    @classmethod
    def setUpClass(cls) -> None:
        cls.ad = Apidemo()

    #读取date.yaml文件，并将读取的数据赋值给data,txt
    @file_data('../data/date.yaml')
    def test_01_login(self,data,txt):

        # 请求数据准备
        url = 'http://v.juhe.cn/laohuangli/d'

        # 模拟请求下发，并接受响应
        res = self.ad.do_post(url=url, data=data)
        # 如果数据格式要求为json
        # res = requests.post(url=url, json=data)

        # 解析响应结果
        print(res.text)
        # 断言，校验预期结果和实际结果
        self.assertEqual(txt,res.json()['reason'],"断言失败")

if __name__ == '__main__':
    unittest.main()