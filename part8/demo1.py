# -*- coding: utf-8 -*-
# @Time : 2021/12/29 22:49
# @Author : jony wang
# @File : demo1.py
'''不可变序列与不可变序列介绍'''
'''可变序列：列表字典'''
lst = [10, 20, 50]
print(id(lst))
lst.append(30)  # 通过append()函数，向列表中添加元素
print(id(lst))  # 添加前后ID不发生变化，说明对象地址不发生变化

'''不可变序列：字符串、字典'''
s = 'hello'
print(id(s))
s = s + 'world'  # 与hello进行连接
print(id(s))  # 添加前后s的ID发生变化
