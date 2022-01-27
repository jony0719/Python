# -*- coding: utf-8 -*-
# @Time : 2021/12/25 0:11
# @Author : jony wang
# @File : demowhile.py

'''判断条件表达式'''
a = 1
if a < 10:
    print(a)  # 条件执行体,判断一次，a小于10，打印a
    a += 1
b = 1
while b < 10:
    print(b)  # 循环体，执行多次，b小于10，重复打印b
    b += 1
