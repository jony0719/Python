# -*- coding: utf-8 -*-
# @Time : 2021/12/18 1:19
# @Author : jony wang
# @File : demo5.py
a = 3.141592
print(a, type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)  # 当然，并不是所有的浮点数据进行计算都会出现小数位不确定的情况,这是二进制底层问题

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
