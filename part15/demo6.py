# -*- coding: utf-8 -*-
# @Time : 2022/1/27 23:08
# @Author : jony wang
# @File : demo3.py

src_file = open('logo.png', 'rb')

target_file = open('copylogo.png', 'wb')

target_file.write(src_file.read())
target_file.close()
src_file.close()
