# -*- coding: utf-8 -*-
# @Time : 2022/1/28 19:49
# @Author : jony wang
# @File : demo17.py

import os.path

print(os.path.abspath('demo13.py'))  # 用于获取文件或目录的绝对路径
print(os.path.exists('demo13.py'), os.path.exists('demo18.py'))  # 用于判断文件或目录是否存在，如果存在返回True，否则返回False
print(os.path.join('D:\\Data\\Python', 'python13.py'))  # 将目录与目录或者文件名拼接起来
print(os.path.split('D:\\Data\\Python\\part15\\demo13.py'))  # 将目录与文件查房
print(os.path.splitext('demo13.py'))  # 将文件与扩展名拆分
print(os.path.basename('D:\\Data\\Python\\part15\\demo13.py'))  # 从一个目录中提取文件名
print(os.path.dirname('D:\\Data\\Python\\part15\\demo13.py'))  # 从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('D:\\Data\\Python\\part15\\demo13.py'))  # 用于判断是否为路径
