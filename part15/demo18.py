# -*- coding: utf-8 -*-
# @Time : 2022/1/28 20:06
# @Author : jony wang
# @File : demo18.py

# 列出制定目录下使用的py文件
import os

path = os.getcwd()  # 获取当前目录
lst = os.listdir(path)  # 获取路径下的所有文件包括目录
for filename in lst:  # 变量文件和目录
    if filename.endswith('.py'):  # 如如果以.py结尾就打印输出
        print(filename)
