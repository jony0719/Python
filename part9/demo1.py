# -*- coding: utf-8 -*-
# @Time : 2022/1/4 22:36
# @Author : jony wang
# @File : demo1.py
'''字符串的驻留机制'''
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))
