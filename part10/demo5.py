# -*- coding: utf-8 -*-
# @Time : 2022/1/9 23:57
# @Author : jony wang
# @File : demo5.py
def fun(a, b=10):  # b称为默认值参数
    print(a, b)


'''函数的调用'''
print(fun(100))
print(fun(20, 30))

print('hello')
print('world')

print('hello', end='\t')  # 指定print()函数的默认值参数，原来为换行。现在替换为制表符。
print('world')
