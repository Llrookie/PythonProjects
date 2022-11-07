import requests

# 请求数据准备
url = 'http://v.juhe.cn/laohuangli/d'

data = {
    "key":"82aecd06c3d7f59f572c7fa57cc1ca85",
    "date":"2022-03-01"
}
# 模拟请求下发，并接受响应
res = requests.post(url=url, data=data)
# 如果数据格式要求为json
# res = requests.post(url=url, json=data)

# 解析响应结果
print(res.text)
# 断言，校验预期结果和实际结果
reason = 'successed'
assert reason == res.json()['reason'], "断言失败"

