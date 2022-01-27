# -*- coding: utf-8 -*-
# @Time : 2022/1/9 3:21
# @Author : jony wang
# @File : demo10.py
s = 'hello,Python'
s1 = s[:5]  # 由于没有指定起始位置，从0开始
s2 = s[6:]  # 由于没有指定结束位置，切到字符串的最后一个元素
s3 = '!'
newstr = s1 + s3 + s2
print(s1)
print(s2)
print(newstr)
print(id(s), id(s1), id(s2), id(s3), id(newstr))

print('===========完整写法,[start:end:step]=============')
print(s[1:5:1])
print(s[::2])
print(s[::-1])  # 默认从字符串的最后一个元素开始，到第一个元素截止。因为步长为负数
print(s[-6::1])  # 截止位置不写，默认到最后一个元素结束
