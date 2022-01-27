# -*- coding: utf-8 -*-
# @Time : 2021/12/31 0:57
# @Author : jony wang
# @File : demo4.py
'''元组的遍历'''
t = ('python', 'hello', 90)
'''第一种方式，使用索引获取元组中的元素'''
print(t[0])
print(t[1])
print(t[2])
'''第二种方式，使用for-in获取元组中的元素'''
for item in t:
    print(item)
