# -*- coding: utf-8 -*-
# @Time : 2022/1/20 0:59
# @Author : jony wang
# @File : demo4.py
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:  # 当不清楚所有的异常，可以BaseException进行捕获，并取名为e
    print('程序出错了', e)
else:
    print('计算结果为：', result)
