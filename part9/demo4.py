# -*- coding: utf-8 -*-
# @Time : 2022/1/5 0:32
# @Author : jony wang
# @File : demo4.py
'''字符串的大小写转换'''
s = 'hello,python'
a = s.upper()
print('原来的字符串:', s, id(s))
print('转换后的字符串:', a, id(a))  # 字符串是不可变序列，转换后产生新的字符串对象

b = s.lower()
print('转换前的字符:', s, id(s))
print('转换后的字符串:', b, id(b))  # 转换之后会产生新的字符串对象
print(b == s)  # 内容相等
print(b is s)  # 地址是不相等的

s2 = 'hello,Python'
c = s2.swapcase()  # 大小转换为小写，小写转换为大写
print('转换前的字符串:', s2)
print('转换后的字符串:', c)

d = s2.title()  # 把每个英文单词的首字母转换为大写，剩余的转换为小写
print('转换前的字符串:', s2)
print('转换后的字符串:', d)
