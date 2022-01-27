# -*- coding: utf-8 -*-
# @Time : 2021/12/21 1:39
# @Author : jony wang
# @File : demoif.py
# 单分支结构
money = 1000
s = int(input('请输入取款金额:'))
if money >= s:
    money = money - s
    #   print('取款:'+s+'元成功','剩余'+money+'元')
    #   整数型进行拼接的时候，需要转换为str类型，否则会报错。
    print('取款:' + str(s) + '元成功,', '剩余' + str(money) + '元')
