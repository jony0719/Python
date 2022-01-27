# -*- coding: utf-8 -*-
# @Time : 2021/12/28 0:45
# @Author : jony wang
# @File : demo4.py
scores = {'张三': 100, '李四': 98, '王五': 45}
'''获取字典所有的键key'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的keys转换成列表

'''获取字典中的所有value'''
values = scores.values()
print(values)
print(type(values))
print(list(values))  # 将所有的values转换成列表

'''获取字典中所有的key-value键值对'''
item = scores.items()
print(item)
print(type(item))  # 输出[('张三', 100), ('李四', 98), ('王五', 45)],实际上是元组
print(list(item))
'''
输出[('张三', 100), ('李四', 98), ('王五', 45)],这个列表中有三个元素
每个元素是一个元组。元组用小括号()表示，小括号里的内容是一个元组
'''
