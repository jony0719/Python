# -*- coding: utf-8 -*-
# @Time : 2022/1/27 23:08
# @Author : jony wang
# @File : demo3.py

file = open('b.txt', 'w')
file.write('Hello World')
file.close()  # 关闭资源

'''
创建b.txt文件，如果b.txt文件不存在则创建，并写入Hello World
如果文件存在，则覆盖原有的内容
'''
