# -*- coding: utf-8 -*-
# @Time : 2021/12/20 22:32
# @Author : jony wang
# @File : demo6.py
# 布尔运算符
a, b = 1, 2
print('==============and运算==================')
print(a == 1 and b == 2)  # True   True and True->True
print(a == 1 and b < 2)  # False  True and False->Flase
print(a != 1 and b == 2)  # False  False and True->False
print(a != 1 and b != 2)  # False  False adn False->False

print('==============or运算====================')
print(a == 1 or b == 2)  # True   只要一个为True，结果就为True
print(a == 1 or b != 2)  # True
print(a != 1 or b == 2)  # True
print(a != 1 or b != 2)  # False

print('===============not（非）运算==============')
# 对bool类型的操作数取反
f1 = True
f2 = False
print(not f1)  # True的取反-》False
print(not f2)  # False的取反-》True

print('================in 和not in===============')
s = 'helloworld'
print('w' in s)  # True
print('k' in s)  # False
print('w' not in s)  # False
print('k' not in s)  # True
