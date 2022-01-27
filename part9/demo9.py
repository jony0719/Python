# -*- coding: utf-8 -*-
# @Time : 2022/1/9 2:01
# @Author : jony wang
# @File : demo9.py
'''字符串的比较操作'''
print('apple' > 'app')  # True
print('apple' > 'banana')  # False

print(ord('a'), ord('b'))  # 使用ord()函数，获取字符的原始值
print(chr(97), chr(98))  # 使用chr()函数，获取原始值对应的字符
print(ord('王'))
print(chr(29579))

'''
==与is的区别
==比较的是原始值是否相等，is比较id是否相等
'''
a = b = 'python'
c = 'python'
print('内存地址:', id(a), id(b), id(c))
print(a == b)
print(b == c)

print(a is b)  # 比较的是内存地址
print(a is c)
