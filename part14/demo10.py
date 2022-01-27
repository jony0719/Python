# -*- coding: utf-8 -*-
# @Time : 2022/1/26 23:35
# @Author : jony wang
# @File : demo10.py
import sys
import time
import os
import urllib.request
import math

print(sys.getsizeof(24))  # 或者对象所占的内存大小
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())  # 返回当前的时间戳，单位为秒
print(time.localtime(time.time()))  # 将秒转换为时间格式

print(urllib.request.urlopen('http://www.baidu.com').read())  # 在进行爬虫的时候会使用

print(math.pi)
