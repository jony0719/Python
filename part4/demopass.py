# -*- coding: utf-8 -*-
# @Time : 2021/12/23 23:36
# @Author : jony wang
# @File : demopass.py
# pass语句，什么都不做，只是一个占位符，用在需要写语句的的地方。
# 举例1：判断是否为会员
answer = input('您是会员吗y/Y')
if answer == 'y' or answer == 'Y':
    pass
else:
    pass
'''
在判断是会员的情况下，执行什么操作；非会员情况下执行什么操作，并未决定好，可用
pass语句来占用，这样程序并不会报错，达到这样一个目的。pass通常会在写语句的时候
'''
