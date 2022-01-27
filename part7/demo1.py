# -*- coding: utf-8 -*-
# @Time : 2021/12/28 0:01
# @Author : jony wang
# @File : demo1.py
'''字典的创建方式'''
'''使用花括号{}进行创建'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(type(scores))

'''使用内置函数dict()创建字典'''
student = dict(name='jony', age=20)
print(student)
print(type(student))

'''创建空字典'''
d = {}
print(d)
