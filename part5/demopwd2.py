# -*- coding: utf-8 -*-
# @Time : 2021/12/25 19:29
# @Author : jony wang
# @File : demopwd2.py
'''使用while循环，从键盘录入密码，超过三次就退出。'''
'''
循环四要素：
1、变量初始化
2、条件判断
3、条件表达式（循环体）
4、改变变量
'''
a = 1
while a <= 3:
    '''条件执行体'''
    pwd = input('请输入您的密码：')
    if pwd == 'password':
        print('恭喜您，密码正确!!!')
        break
    else:
        print('密码不正确!!!')
    '''改变变量'''
    a += 1
