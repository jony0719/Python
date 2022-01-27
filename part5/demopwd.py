# -*- coding: utf-8 -*-
# @Time : 2021/12/25 18:48
# @Author : jony wang
# @File : demopwd.py
'''举例1：从键盘录入密码，最多录入三次，如果三次都不正确就退出程序。'''
'''
pwd = input('请输入密码:')
for i in range(10):
    if pwd == 'password':
        print('密码正确')
    elif pwd != 'password':
        print('密码不正确')
    elif i >= 3:
        break
'''
for i in range(3):
    pwd = input('请输入密码:')
    if pwd == 'password':
        print('密码正确')
        break
    else:
        print('密码不正确')
'''
注意:
pwd = input('请输入密码:')需要写在for-in循环中，这样密码不正确，需要循环重复输入。
当密码正确，就退出程序
'''