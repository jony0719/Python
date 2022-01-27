# -*- coding: utf-8 -*-
# @Time : 2022/1/9 1:38
# @Author : jony wang
# @File : demo8.py

'''使用replace()方法，字符串的替换'''
s = 'hello,python'
print(s.replace('python', 'java'))  # 使用java替换python

s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))  # 使用第3个参数，指定替换的次数
print(s1)  # 替换前的字符串不发生变化

'''使用join()方法，进行字符串的替换'''
lst = ['hello', 'java', 'python']  # 前提是列表或者元组
print('|'.join(lst))  # 使用|将列表中的元素进行连接
print(''.join(lst))  # 使用空，将列表中的元素进行连接

t = ('hello', 'java', 'python')  # 将元组的数据进行连接
print(''.join(t))

print('#'.join('python'))
