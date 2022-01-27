# -*- coding: utf-8 -*-
# @Time : 2021/12/25 20:50
# @Author : jony wang
# @File : demoelse2.py
i = 1
while i <= 3:
    pwd = input('请输入您的密码:')
    if pwd == 'password':
        print('恭喜您，密码正确')
        break
    else:
        print('对不起，密码错误')
    i += 1
else:
    print('对不起，密码已输入3次')
