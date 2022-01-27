# -*- coding: utf-8 -*-
# @Time : 2021/12/29 23:01
# @Author : jony wang
# @File : demo2.py
'''元组的创建方式'''
'''第一种方式，直接使用()进行创建'''
t = ('python', 'hello', 98)
print(t)
print(type(t))

'''第二种方式，使用内置函数tuple()'''
t1 = tuple(('hello', 'world', 80))
print(t1)
print(type(t1))

'''或者使用下列方式,省略小括号'''
t2 = 'hello', 'world', 101  # 使用这种方式可以省略小括号
print(t2)
print(type(t2))

'''只有一个元素的元组，需要使用小括号，才表示为元组数据'''
'''
t3 = ('python')  # 如果元组中只有一个元素，逗号不能省略
print(t3)
print(type(t3))
'''
t3 = ('python',)
print(t3)
print(type(t3))

'''空元组的创建方式'''
'''空列表的创建方式'''
lst = []
lst1 = list()

d = {}
d2 = dict()

# 空元组
t4 = ()
t5 = tuple()
print('空列表', lst, lst1)
print('空字典', d, d2)
print('空元组', t4, t5)
