# -*- coding: utf-8 -*-
# @Time : 2022/1/28 17:05
# @Author : jony wang
# @File : demo16.py

# os模块操作目录的相关函数
import os

print(os.getcwd())  # 获取当前的工作目录

lst = os.listdir('../part15')  # 返回指定路径下的文件和目录信息
print(lst)

# os.mkdir('newdir2')  # 创建目录
# os.makedirs('A/B/C')  # 创建多级目录

# 删除目录
# os.rmdir('newdir2')  # 删除目录
# os.removedirs('A/B/C')  # 删除多级目录

os.chdir('D:\\Data\\Python\\part15')  # 设置当前工作目录
print(os.getcwd())
