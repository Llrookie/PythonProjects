# class grandFather:
#     name = '老张'
#     def eat1(self):
#         print('grandFather : eat')
#
# class Father1(grandFather):
#     name = '张1'
#     def eat1(self):
#         print('Father1 : eat')
#
# class Father2:
#     name = '张2'
#     def eat(self):
#         print('Father2 : eat')
#
# class Son(Father1,Father2):
#     name = '小章'
#     def eat1(self):
#         print('son : eat')
#
# if __name__ == '__main__':
#     son = Son()
#     son.eat()

# class father:
#     def study(self):
#         print('father : study')
# class son(father):
#     def study(self):
#         print('son : study')
#     def sleep(self):
#         print('son : sleep')
#         super().study()
# if __name__ == '__main__':
#     s = son()
#     s.sleep()

# class Person:
#     def __init__(self):     #构造方法
#         print('this is init()')
#         self.name = 'zhangsan'
#         self.__age = 18   ##私有属性，只能在类的内部调用
#     def __study(self):   #私有方法，只能在类的内部调用
#         print('this is study()')
#     def sleep(self):
#         print('this is sellp()')
#         print(self.__age)
#         self.__study()
#
#     def __del__(self):      #析构方法
#         print('this is del()')
#
# if __name__ == '__main__':
#     p = Person()
#     p.sleep()

class Father:
    def study(self):
        print('father study()')

class Son(Father):
    def study(self):
        print('son study()')

if __name__ == '__main__':
    def method(obj):
        obj.study()
    fa = Father()
    son = Son()
    method(fa)
    method(son)