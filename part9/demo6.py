# -*- coding: utf-8 -*-
# @Time : 2022/1/9 0:38
# @Author : jony wang
# @File : demo6.py
'''字符串的分隔'''

'''split()，从左侧开始劈分'''
s = 'hello world Python'
lst = s.split()  # 默认的劈分字符串是空格。
print(lst)  # 返回的是一个列表

s1 = 'hello|world|Python'
print(s1.split())  # 默认的劈分字符串是空格，所以输出的还是原字符
print(s1.split(sep='|'))  # 指定|作为分隔符，输出的是字符串
print(s1.split(sep='|', maxsplit=1))

'''rsplit()，从右侧开始劈分'''
print(s.rsplit())  # 从右侧开始劈分，未指定默认是空格
print(s1.rsplit(sep='|'))
# print(s1.rsplit('|'))  # 或者不适用sep参数，直接在rsplit()在括号中使用'|'
print(s1.rsplit(sep='|', maxsplit=1))
