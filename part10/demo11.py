# -*- coding: utf-8 -*-
# @Time : 2022/1/19 0:20
# @Author : jony wang
# @File : demo11.py
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 函数的调用
print(fib(6))
print('=============输出斐波那契数列===================')
'''要求输出这个数列上的前六位数字'''
for i in range(1, 7):
    print(fib(i))
