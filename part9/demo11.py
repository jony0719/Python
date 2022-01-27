# -*- coding: utf-8 -*-
# @Time : 2022/1/9 3:55
# @Author : jony wang
# @File : demo11.py
'''格式字符串的第一种方式，使用%'''
name = '张三'
age = 18
print('我的名字叫%s,今年%d岁了' % (name, age))  # 元组

'''格式化字符串的第二种方式，使用{}'''
print('我的名字叫{0},今年{1}岁了'.format(name, age))  # 方法

'''py3中使用f-string来格式化字符串'''
print(f'我的名字叫{name},今年{age}岁了')
