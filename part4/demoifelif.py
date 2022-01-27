# -*- coding: utf-8 -*-
# @Time : 2021/12/22 23:37
# @Author : jony wang
# @File : demoifelif.py

# 多分支结构
'''
从键盘录入一个整数表示成绩，判断成绩的等级。
90-10   A
80-90   B
70-80   C
60-70   D
0-59    E
小于0或者大于100，为非法的数据（不是合法的成绩范围）
'''
n = int(input('请输入一个分数：'))
if n >= 90 and n <= 100:
    print('成绩优秀:等级A,', '分数' + str(n))
elif n >= 80 and n < 90:
    print('成绩良:等级B,，', '分数' + str(n))
elif n >= 70 and n < 80:
    print('成绩中:等级C,', '分数' + str(n))
elif n >= 60 and n < 70:
    print('成绩差:等级D,', '分数' + str(n))
elif n >= 0 and n < 60:
    print('成绩不及格:等级E,', '分数' + str(n))
else:
    print('请输入合法的成绩！')
