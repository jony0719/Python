# -*- coding: utf-8 -*-
# @Time : 2022/1/21 0:52
# @Author : jony wang
# @File : demo10.py
# print(10 / 0)
import traceback

try:
    print('=================')
    print(1 / 0)
except:
    traceback.print_exc()
