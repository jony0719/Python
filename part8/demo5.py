# -*- coding: utf-8 -*-
# @Time : 2022/1/3 20:18
# @Author : jony wang
# @File : demo5.py
'''集合的创建方式'''

'''第一种创建方式，使用{}'''
s = {2, 3, 4, 5, 5, 6, 7, 7}
print(s)  # 集合和字典是相同的数据结构，key值不能重复。

'''第二种创建方式，使用内置函数set()'''
s1 = set(range(6))  # range(6),会产生一个0-6的整数列表。
print(s1, type(s1))

s2 = set([1, 2, 3, 4, 5, 5, 6, 6])  # 使用set()函数，将列表转换为集合
print(s2, type(s2))

s3 = set((1, 2, 4, 4, 5, 65))
print(s3, type(s3))  # 使用set()函数，将元组转化为集合

s4 = set('python')  # 使用set()函数，将字符串转换为集合
print(s4, type(s4))

s5 = set({12, 4, 34, 55, 66, 44, 4})  # {}本身就是集合，set()函数将集合转换为集合
print(s5, type(s5))

'''定义一个空集合'''
s6 = {}  # 定义空集合的时候，不能使用这种方式，这样表示定义一个空字典。
print(s6, type(s6))

s7 = set()
print(s7, type(s7))
