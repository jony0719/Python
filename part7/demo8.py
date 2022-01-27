# -*- coding: utf-8 -*-
# @Time : 2021/12/29 22:24
# @Author : jony wang
# @File : demo8.py
items = ['fruits', 'books', 'others']
prices = [96, 78, 85]
'''zip()函数将对应的元素，打包成一个元组'''
print(list(zip(items, prices)))

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

'''如果两个列表元素的数目不相等，会出现什么情况'''

