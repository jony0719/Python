# -*- coding: utf-8 -*-
# @Time : 2022/1/28 0:44
# @Author : jony wang
# @File : demo10.py
file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
