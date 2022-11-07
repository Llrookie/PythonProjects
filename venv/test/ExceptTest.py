# print(10/0)     #ZeroDivisionError
# print(1 +'a')   #TypeError
# print(a)        #NameError
import sys

# try:
#     print('11111')
#     print(10/0)
#     print('33333')
# except Exception as e:
#     print(e)
# else:
#     print('this is else')
# finally:
#     print('this is finally')
# print('22222222')

for i in range(1,11):
    if i == 5:
        try:
            raise TypeError('自定义异常！')
        except Exception as e:
            break
    else:
        print(i)