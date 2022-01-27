# -*- coding: utf-8 -*-
# @Time : 2021/12/25 20:15
# @Author : jony wang
# @File : democontinue.py
'''使用continue，要求输出1-50之间，所有5的倍数'''
'''
思路：什么是5的倍数？
能被5整数，余数为0的数。
不能被5整除，余数部位0的数。
'''
for i in range(1, 51):
    if i % 5 == 0:
        print('5的倍数:', i)

print('=========使用continue，输出5的倍数==============')
for i in range(1, 51):
    if i % 5 != 0:
        continue
    else:
        print('5的倍数', i)
