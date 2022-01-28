# -*- coding: utf-8 -*-
# @Time : 2022/1/28 20:12
# @Author : jony wang
# @File : dmeo19.py

# 递归遍历目录以及目录下子文件
import os

path = os.getcwd()
lst_files = os.walk(path)  # 迭代器对象
print(lst_files)  # <generator object _walk at 0x000002458A3B5D20>
for dirpath, dirname, filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('================================================')'''
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in filename:
        print(os.path.join(dirpath, file))
    print('=================================================')
