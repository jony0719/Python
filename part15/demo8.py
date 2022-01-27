# -*- coding: utf-8 -*-
# @Time : 2022/1/27 23:08
# @Author : jony wang
# @File : demo3.py

file = open('c.txt', 'a')
# file.write('hello')
lst = ['Java', 'Go', 'Python']
file.writelines(lst)  # 将字符串列表s_list写文本文件，不添加换行符
file.close()
