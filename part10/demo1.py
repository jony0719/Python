# -*- coding: utf-8 -*-
# @Time : 2022/1/9 19:27
# @Author : jony wang
# @File : demo1.py
'''函数的定义'''


def calc(a, b):
    c = a + b
    return c


'''函数的调用的第一种方法'''
result = calc(10, 20)  # 10,20称为实际参数的值，简称为实参，实参的位置是在函数的调用处。
print('result的结果是:', result)

'''函数调用的第二种方法'''
result1 = calc(b=20, a=10)  # 等号左侧的a,b变量名称称为关键字参数
print('result1的结果是:', result1)
