# -*- coding: utf-8 -*-
# @Time : 2021/12/26 22:45
# @Author : jony wang
# @File : demo4.py
print('p' in 'python')  # True
print('k' not in 'python')  # True

'''判断指定元素是否在列表中'''
lst = [10, 20, 30, 40, 50]
print(10 in lst)  # True
print(60 in lst)  # False
print(10 not in lst)  # False
print(60 not in lst)  # True

'''列表元素的遍历'''
'''从列表对象中依次取出元素赋值给i'''
for i in lst:
    print(i)
