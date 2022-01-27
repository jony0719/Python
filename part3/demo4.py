# -*- coding: utf-8 -*-
# @Time : 2021/12/19 0:20
# @Author : jony wang
# @File : demo4.py

# 赋值运算符，执行顺序从右到左。
i = 3 + 4
print(i)

# 支持链式赋值
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 支持参数赋值
print('==========支持参数赋值========')
a = 20
a += 20  # 相当于a+20再赋值给a,即a=a+20
print(a, type(a))
a -= 20
print(a, type(a))
a *= 3
print(a, type(a))
a /= 2
print(a, type(a))
a //= 20
print(a, type(a))
a % 20  # 1/20的商为0，余数为1
print(a, type(a))

# 支持系列解包赋值
print('=========支持系列解包赋值==========')
a, b, c = 30, 40, 50  # 变量个数必须要与值的个数一致，否则会报错。
print(a, b, c)

# 解包赋值的好处，实现两个变量值的互换。
print('============交换两个变量的值=======')
a = 20
b = 30
print('交换之前的值：', a, b)
print('=============交换之后的值===========')
a, b = b, a
print('交换之后的值：', a, b)
