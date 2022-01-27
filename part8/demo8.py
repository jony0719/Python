# -*- coding: utf-8 -*-
# @Time : 2022/1/3 21:58
# @Author : jony wang
# @File : demo8.py
'''集合的数学操作'''
'''（1）交集操作'''
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print('s1与s2的交集:', s1.intersection(s2))
print('s1与s2的交集:', s1 & s2)  # intersection()与&符号是等价的。
print(s1)
print(s2)

'''（2）并集操作'''
print('s1与s2的并集:', s1.union(s2))
print('s1与s2的并集:', s1 | s2)  # union()方法与|是等价的。
print(s1)
print(s2)

'''（3）差集操作'''
print('s1与s2的差集:', s1.difference(s2))
print('s1与s2的差集:', s1 - s2)  # difference()与-是相等的。
print(s1)
print(s2)

'''（4）对称差集操作'''
print('s1与s2对称差集:', s1.symmetric_difference(s2))
print('s1与s2对称差集:', s1 ^ s2)  # symmetric_difference()与^是等价的。
print(s1)
print(s2)
