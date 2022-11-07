#定义一个类，实现加减乘除

class myMath1():

    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def ride(self,a,b):
        return a * b

    def div(self,a,b):
        if a == 0:
            return "error"
        else:
            return a / b