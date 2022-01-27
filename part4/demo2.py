# -*- coding: utf-8 -*-
# @Time : 2021/12/21 0:35
# @Author : jony wang
# @File : demolist.py
# 测试对象的布尔值
print('==========以下对象的布尔值均为False=======================')
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))  # 空字符串
print(bool(""))  # 空字符串

print(bool([]))  # 空列表
print(bool(list()))  # 空列表

print(bool())  # 空元组
print(bool(tuple()))  # 空元组

print(bool({}))  # 空字典
print(bool(dict()))

print(bool(set()))  # 空集合

print('=============其他对象的布尔值均为True=======================================')
print(bool(18))
print(bool(True))
print(bool('helloworld'))
