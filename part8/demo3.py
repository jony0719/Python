# -*- coding: utf-8 -*-
# @Time : 2021/12/31 0:38
# @Author : jony wang
# @File : demo3.py
t = (10, [20, 30], 90)
print(t)
print(type(t))  # 为元组类型

'''查看元组的数据、数据类型、ID(内层地址)'''
print(t[0], type(t[0]), id(t[0]))  # t[0]=10，为int类型
print(t[1], type(t[1]), id(t[1]))  # t[1]=[20,30],为列表类型
print(t[2], type(t[2]), id(t[2]))  # t[2]=90,为int类型

'''尝试将t[1]修改为100'''
print(id(100))
# t[1] = 100  # 元组是不被允许修改元素的！！！
'''
由于t1=[20,30]是列表，列表是可变序列，所以可以向列表中添加元素,而列表的内存地址不变
'''
t[1].append(100)  # 向列表中添加元素，但是ID是不变的
print(t[1], type(t[1]), id(t[1]))
