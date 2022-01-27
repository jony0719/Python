# -*- coding: utf-8 -*-
# @Time : 2021/12/24 0:25
# @Author : jony wang
# @File : demo1.py
'''range对象创建的三种方式'''
'''第一种创建方式，range(stop)'''
r = range(10)  # 创建一个(0,10)之间的序列（不包含10），默认步长为1
print(r)  # 输出为:range(0,10),range()函数的返回值是迭代器对象，无法看到序列的数据。
print(list(r))  # 需要使用list()函数可以列出序列，并打印出来。

'''第二种创建方式，range(start,stop)'''
r = range(1, 10)  # 创建一个(1,10)的序列（不包含10），默认步长为1
print(list(r))

'''第三种创建方式，range(start,stop,step)'''
r = range(1, 10, 2)  # 创建一个(0,10)的序列（不包含10），步长指定为2
print(list(r))

'''使用not和not in来判断指定数是否在序列中'''
'''通常会使用range()作为for-in循环的变量对象'''
r = range(1, 10, 2)
print(3 in r)  # True
print(4 in r)  # False
print(4 not in r)  # True
print(3 not in r)  # False
