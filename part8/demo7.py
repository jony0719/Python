# -*- coding: utf-8 -*-
# @Time : 2022/1/3 21:23
# @Author : jony wang
# @File : demo7.py
'''集合间的关系'''

'''两个集合是否相等'''
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)
print(s1 != s2)

'''一个集合是否是另外一个集合的子集'''
s1 = {10, 20, 30, 40, 50, 60, }
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print('s2是s1的子集吗？', s2.issubset(s1))
print('s3是s1的子集吗？', s3.issubset(s1))

'''一个集合是否是另外一个集合的超集'''
'''B是A的子集，那么A是B的超集'''
print('s1是s2的超集吗？', s1.issuperset(s2))
print('s1是s3的超集吗？', s1.issuperset(s3))

'''两个集合是否没有交集'''
print('s1与s2没有交集吗？', s1.isdisjoint(s2))
print('s1与s3没有交集吗？', s1.isdisjoint(s3))
