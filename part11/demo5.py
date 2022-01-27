# -*- coding: utf-8 -*-
# @Time : 2022/1/20 0:59
# @Author : jony wang
# @File : demo4.py
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('相除的结果为：', result)
except ZeroDivisionError:
    print('对不起，除数不能为0')
print('程序结束')
