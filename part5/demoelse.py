# -*- coding: utf-8 -*-
# @Time : 2021/12/25 20:41
# @Author : jony wang
# @File : demoelse.py
for i in range(3):
    pwd = input('请输入您的密码:')
    if pwd == 'password':
        print('恭喜您，密码输入正确')
        break
    else:
        print('密码输入错误 ')
else:
    '''密码输入错误3次后，退出循环，打印的内容'''
    print('对不起，密码输入3次')
