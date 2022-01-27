# -*- coding: utf-8 -*-
# @Time : 2022/1/3 22:18
# @Author : jony wang
# @File : demo9.py
'''列表生成式'''
lst = [i * i for i in range(6)]
print(lst, type(lst))

'''集合生成式'''
s = {i * i for i in range(10)}
print(s, type(s))
