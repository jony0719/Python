# -*- coding: utf-8 -*-
# @Time : 2021/12/18 21:49
# @Author : jony wang
# @File : add.py

# 第一种方式
# n1=input('请输入第一个数')
# n1=int(n1)
# n2=input('请输入第二个数')
# n2=int(n2)
# print(n1+n2)

# 第二种方式
# 从键盘录入两个整数，并计算两个数的和。
# n1=input('请输入第一个数：')
# n2=input('请输入第二个数：')
# print(n1,n2,type(n1),type(n2))  #输入的数据类型为str类型，需要进行转换。
# print(int(n1),int(n2),type(int(n1)),type(int(n2)))
# print(int(n1)+int(n2))

# 第三种方式。
n1 = int(input('请输入第一个数：'))  # 将输入的为str的数据类型直接进行转换。
n2 = int(input('请输入第二个数：'))
print(n1, n2, type(n1), type(n2))
print(n1 + n2)

# 说明：
# 可以在输入的时候进行转换，也可以在输入之后进行转换。
