# -*- coding: utf-8 -*-
# @Time : 2021/12/22 23:17
# @Author : jony wang
# @File : demoifelse.py

# 从键盘录入一个整数，让程序判断是基数还是偶数。
num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(str(num) + '是偶数')
else:
    print(str(num) + '是奇数')
