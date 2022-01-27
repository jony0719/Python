# -*- coding: utf-8 -*-
# @Time : 2021/11/28 21:49
# @Author : jony wang
# @File : demo1.py

# 输出数字
print(520)
print(520.14)

# 输出字符串
print('helloworld')
print("helloworld")

# 输出含有运算符的表达式
# 操作数+运算符组成表达式，这里3和1为操作数，+代表运算符
print(3 + 1)

# 将内容输出到文件中
fp = open('/part1/a.txt', 'a+')  # a+表示如果文件不存在就创建，存在就追加
print('helloworld', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行中）
print('hello', 'world', 'python')  # 使用逗号分隔会在一行当中输出内容
