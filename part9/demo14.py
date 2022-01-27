# -*- coding: utf-8 -*-
# @Time : 2022/1/9 4:33
# @Author : jony wang
# @File : demo14.py
'''#1，编码'''
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK编码格式中，一个中文占用2个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8编码格式中，一个中文占用3个字节

'''#2，解码'''
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码，byte表示的就是二进制数据(字节类型的数据)

byte = s.encode(encoding='UTF-8')  # 用UTF-8编码
print(byte.decode(encoding='UTF-8'))  # 使用UTF-8解码
