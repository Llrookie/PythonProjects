import requests

'''
    接口的关键字驱动，是业内主流的接口框架的设计模式
    将常用的请求方法进行函数的封装，以便于后续的可复用性和易于维护的性质
'''

class Apidemo:
    # POST
    # 将data和headers默认为空，有值传值
    def do_post(self,url,data = None,headers = None, **kwargs):
        return requests.post(url=url,data=data,headers=headers,**kwargs)

    # GET
    def do_get(self,url,data = None,headers = None,**kwargs):
        return requests.post(url=url,params=data,headers=headers,**kwargs)
