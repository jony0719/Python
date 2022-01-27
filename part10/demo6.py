# -*- coding: utf-8 -*-
# @Time : 2022/1/10 0:14
# @Author : jony wang
# @File : demo6.py
def fun(*args):  # 函数定义时的可变的位置参数
    print(args)
    # print(args[0])


fun(10)
fun(10, 30)
fun(10, 30, 40)


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=20, b=30, c=40)
print('hello', 'world', 'java')


# def fun3(*args, *a):  # 定义位置可变的位置参数，只能是1个
# pass

# def fun2(**args,**args):  # 定义个数可变的关键字参数，只能是1个
# pass

def fun2(*args1, **args2):
    pass


# def fun3(**args1,*args2):
#   pass

'''
总结：
在一个函数的定义过程中，既有个数可变的关键字形参，又有个数可变的位置形参。
要求，格式可变的位置形参，放在个数可变的关键字形参之前
'''
