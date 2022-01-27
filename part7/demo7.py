# -*- coding: utf-8 -*-
# @Time : 2021/12/29 22:04
# @Author : jony wang
# @File : demo7.py
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
lst = zip(items, prices)
print(list(lst))


d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
