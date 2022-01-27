# -*- coding: utf-8 -*-
# @Time : 2022/1/18 22:03
# @Author : jony wang
# @File : demo10.py
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))
