# -*- coding: utf-8 -*-
# @Time : 2022/1/27 23:08
# @Author : jony wang
# @File : demo3.py
# 将磁盘上a.txt的文件打开
file = open('a.txt', 'r')  # 磁盘上的文件就创建在了python中的一个对象
print(file.readlines())  # 读取文件内容，readlines()结果是一个列表，会读取问价中的所有内容
file.close()  # 关闭资源
# 把读取到的两行内容放在一个列表中
