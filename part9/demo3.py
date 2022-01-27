# -*- coding: utf-8 -*-
# @Time : 2022/1/4 23:29
# @Author : jony wang
# @File : demo3.py
'''字符串的查询操作'''
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# print(s.index('k'))  # 查找字符串第一次出现k的位置，如果不存在的时候，会抛出异常。
print(s.find('k'))  # 查找字符串第一次出现k的位置，如果不存在不会抛出异常。建议使用find()方法，因为不会抛出异常

#  print(s.rindex('k'))  # 查找最后一次出现k的位置，如果不存在则会抛出异常
print(s.rfind('k'))  # 查找最后一次出现k的位置，如果不存在不会抛出异常。建议使用find()方法。
