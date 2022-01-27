# -*- coding: utf-8 -*-
# @Time : 2022/1/26 20:13
# @Author : jony wang
# @File : demo4.py
# 导入模块的第二种方式
import math
from math import pi  # 只是导入math中的pi

print(pi)
print(pow(2, 3))  # 这里的pow并不是math中的pow,因为只是导入了math中的pi，并没有导入math中的pow
print(math.pow(2, 8))
