# -*- coding: utf-8 -*-
# @Time : 2021/12/25 20:34
# @Author : jony wang
# @File : demo.py

'''与else语句配合使用的三种情况'''
'''if语句表达式不成立时，执行else'''
if ...:
    ...
else:
    ...

'''没有碰到break时，执行else'''
'''循环的正常执行次数执行完成，就会执行else'''
while ...:
    ...
else:
    ...

for i in ...:
    ...
else:
    ...

'''嵌套循环'''
while ...:
    ...
    for i in ...:
        ...
    else:
        ...
