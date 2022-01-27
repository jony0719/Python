# -*- coding: utf-8 -*-
# @Time : 2022/1/26 20:05
# @Author : jony wang
# @File : demo3.py
# 导入模块
import math  # 关于数学运算的模块

print(id(math))
print(type(math))
print(math)

# 使用模块
print(math.pi)  # 使用模块，输出圆周率
print('============================================================')
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))  # 计算2的3次方
print(math.ceil(9.001))  # 取最接近的最大整数10
print(math.floor(9.99999))  # 取最接近的最小的整数9
