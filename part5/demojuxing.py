# -*- coding: utf-8 -*-
# @Time : 2021/12/25 22:16
# @Author : jony wang
# @File : demojuxing.py
'''输出一个三行四列的矩形'''
'''
思路:
什么是矩形？
首先要执行四次。
'''
'''打印行'''
'''
for i in range(3):
'''
'''打印列,打印四列后就换行'''
'''
    for j in range(4):
        print('1', end='')
    else:
        print('\n')
'''
'''for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()'''

'''打印边长为3的等角三角'''
'''
什么是等角三角形？
行和列长度的长度都为3
。。。
。。
。
'''
'''外层循环打印行'''
'''
for i in range(1, 9):
    if i == 1:  # 打印第一行
        print('*')
    elif i == 2:  # 打印第二行
        for j in range(1, i + 1):
            print('*', end='\t')
        print()
    elif i == 3:  # 打印第三行
        for k in range(1, i + 1):
            print('*', end='\t')
        print()
'''
'''打印9*9的直角三角形'''
"""
for i in range(1, 10):
    '''第一行打印一个*，第二行打印2个*'''
    for j in range(1, i + 1):
        print('*', end='\t')
    print()
"""

'''打印9*9乘法表'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', j * i, end='\t')
        # print(str(j) + '*' + str(i) + '=' + str(j * i), end='\t')
    print()
