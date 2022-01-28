# -*- coding: utf-8 -*-
# @Time : 2022/1/28 16:31
# @Author : jony wang
# @File : demo14.py

# with语句实现文件的复制,不需要手动写关闭文件过程
with open('logo.png', 'rb') as src_file:
    with open('copy2logo.png', 'wb') as target_file:
        target_file.write(src_file.read())
