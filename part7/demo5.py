# -*- coding: utf-8 -*-
# @Time : 2021/12/28 1:01
# @Author : jony wang
# @File : demo5.py
"""字典元素的遍历"""
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:  # item是字典元素的键
    print(item)

'''遍历字典元素的的key-value'''
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:  # item是字典元素的键
    print(item, scores[item], scores.get(item))
