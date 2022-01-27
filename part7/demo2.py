# -*- coding: utf-8 -*-
# @Time : 2021/12/28 0:11
# @Author : jony wang
# @File : demo2.py
'''获取字典中的元素'''
'''第一种方式，使用[]获取字典中的元素'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores['张三'])
# print(scores['陈六'])  # 当字典中中不存在名为python的key后，抛出KeyError

'''第二种方式，使用get()方法获取字典中的元素'''
print(scores.get('李四'))
print(scores.get('陈六'))  # 字典中不存在指定的key后，不会报错。而是返回None
print(scores.get('麻七', 99))  # 可以通过参数设置返回指定值，如99
