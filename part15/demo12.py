# -*- coding: utf-8 -*-
# @Time : 2022/1/28 14:43
# @Author : jony wang
# @File : demo12.py
# with语句讲解,不用手动关闭文件，避免造成资源浪费
print(type(open('a.txt', 'r')))
with open('a.txt', 'r') as file:
    print(file.read())
