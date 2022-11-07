# str1 = 'hello heby'
# str2 = 'world'
# str3 = str1 + str2
# print(str3)
# print(str1.replace('he','baby',1))
# print(str1.replace('he','baby',2))
# # print(str3)
#
# set1 = {}
# print(type(set1))
# set2 = set()
# print(type(set2))

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1 | set2)
# print(set1 - set2)
# print(set1 & set2)
# print(set1)
# set1.pop(1)
# print(set1)

# dict1 = {'name':'张三','age':18,'name':'李四'}
# print(dict1)
# dict1['age'] = 28   #修改键值为age的值
# print(dict1)
# print(dict1['name'])  #无序，不支持下标
# print(dict1.keys())   #获取所有的key值
# print(dict1.values())  #获取所有的value值
# print(dict1.get('name'))  #根据key值获取value值
# dict1.pop('name')  #删除指定的键值对
# print(dict1)
# dict1.clear()  #清空字典

# set1 = {'zhang','lisi','wu'}
# set2 = {'lisi','liu'}
# set1.update(set2)
# print(set1)

# a = '5'
# b = int(a)
# print(a,b)
# print(type(a),type(b))

# a = '1 + 2'
# b = eval(a)
# print(a,b)
# print(type(a),type(b))

# a = 'zhangsan'
# b = dict.fromkeys(a,10)
# print(a,b)
# print(type(a),type(b))

# a = 9
# print(bin(a))
# print(oct(a))
# print(hex(a))

###########################运算符#################################
#1、算符运算符
# print(5/2)
# print(5.0//2)
# print(5%2)
# print(5 ** 2)
# print(pow(5,2))

# a = {1:2,2:3}
# b = {1:2,2:'3'}
# print(a == b)

# a = 9
# print(~ a)
# print(a << 2)
# print(a >> 2)

# str1 = 'zhangsan'
# for i in str1:
#     print(i,end="")

# list1 = ['a','b','c']
# if 'b' in list1:
#     print("yes")
# else:
# #     print('no')
#
# a = 'string1'
# b = 'string1'
# print(id(a),id(b))
# print(type(a),type(b))
# print(a is b)
# print(a == b)
# a = 5
# if a > 5:
#     if a == 8:
#         print("a = 8")
#     else:
#         print("a != 8")
# else:
#     print("a < 5")

# list1 = ['a','b','c','d']
# for i in list1:
#     if i == 'cc':
#         print(i)
#         break
#     print("循环数据",i)
# else:
#     print("未找到循环数据")

# def print_name(name):
#     print(name)
# # print_name("helle world")
#
# def area(weight,heignt):
#     print_name("函数嵌套")
#     return weight * heignt
#
# sum = area(5,4)
# print(sum)

# def method1(x,y):
#     return x+y,x*y,x-y,x/y
# result = method1(5,2)
# result1,result2,result3,result4 = method1(5,2)
# print(result)
# a = 10
# print(id(a))
# a = 20
# print(id(a))

# a = 1
# def method(a):
#     a = 2
#     print(a)
# method(a)
# print(a)
#
# def me(x,y):
#     '''
#
#     :param x:
#     :param y:
#     :return:
#     '''
# print(me.__doc__)
# def method(age1,age2):
#     print("姓名是：%d,年龄是：%d"%(age1,age2))
# method(18)

# def add(*number):
#     total = 0
#     for i in number:
#         total += i
#     return total
# if __name__ == "__main__":
#     print(add(1,2,3))

# sum = lambda x,y:x+y
# if __name__ == "__main__":
#     print(sum(2,3))

# li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
# li=sorted(li, key=lambda x:x["age"])
# print(li)

# import package1.module1 as ee
# import package1.module2 as cc
from package1.module2 import test
import os

# path = os.getcwd()
# path = os.path.abspath('.')
# print(path)
# if __name__ == '__main__':
#     # ee.method()
#     cc.test().method3()


def test(x,y):
    a = x + y
    return a

if __name__ == '__main__':
   result =  test(2,4)
   print(result)

filename = os.path.dirname(__file__)
print(filename)
















