# -*- coding: utf-8 -*-
# @Time : 2022/1/26 21:32
# @Author : jony wang
# @File : demo9.py
# 在导入带有包的模块时，注意事项
import package1  # 在使用import方式导入时，只能跟包名或模块名
import calc
# 在使用from...import可以导入包、模块、函数、变量
from package1 import module_A
from package1.module_A import a

print(a)
