# -*- coding: utf-8 -*-
# @Time : 2021/12/26 21:02
# @Author : jony wang
# @File : demolist2.py
'''获取列表单个元素，给一个指定的索引，在列表中查看是否存在'''
lst = ['hello', 'world', 98, 'hello', 'world', 234]
'''获取索引为1的元素,获取索引为-2的元素;正向从0到N-1，逆向从-N到-1'''
print(lst[1], lst[-2])

'''获取索引为10的元素'''
# print(lst[10])    # IndexError: list index out of range
