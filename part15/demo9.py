# -*- coding: utf-8 -*-
# @Time : 2022/1/27 23:08
# @Author : jony wang
# @File : demo3.py

file = open('a.txt', 'r')
# file.seek(1)  # 参数为1的时候会报错，因为一个汉字占两个字节
file.seek(2)
print(file.read())
print(file.tell())  # 返回文件指针的当前位置
file.close()
