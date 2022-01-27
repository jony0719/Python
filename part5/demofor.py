# -*- coding: utf-8 -*-
# @Time : 2021/12/25 2:28
# @Author : jony wang
# @File : demofor.py
'''
依次取出，字符串python的元素，并自动赋值给item，直到取完所有的元素，退出循环体
第一次，取出p,并自动赋值给item
第二次，取出y,并自动赋值给item
依次。。。。。。
'''
for item in 'python':
    print(item)

'''range()可以产生整数序列'''
for i in range(10):
    print(i)

'''如果循环体内，不需要使用自定义变量，可以使用下划线(_)代替'''
for _ in range(5):
    print('人生苦短，我用python。')

'''使用for循环，计算1-100的偶数和'''
'''
循环四要素
1、变量初始化
2、判断条件
3、条件表达式（循环体）
4、改变变量
'''
sum = 0
for i in range(1, 101):  # 这里i的初始值为1
    '''需要定义一个为sum的变量，用于存储偶数和'''
    if i % 2 == 0:
        sum = sum + i
print('1-100的偶数和为:', sum)
