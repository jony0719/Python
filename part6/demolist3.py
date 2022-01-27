# -*- coding: utf-8 -*-
# @Time : 2021/12/26 21:17
# @Author : jony wang
# @File : demolist3.py
lst = [10, 20, 30, 40, 50, 60, 70, 80]
# start为1，stop为6
# print(lst[1:6:1])
print('原列表：', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[1:6])  # 默认步长为1
print(lst[1:6:])

'''start为1，stop为6，步长为2'''
print(lst[1:6:2])
'''start省略，stop为6，步长为2'''
print(lst[:6:2])  # 默认start为0
'''star为1，stop省略，步长为2'''
print(lst[1::2])

print('==============step为负数的情况==============')
print('原列表:', lst)
'''start和stop都默认省略，step=-1。默认从最后一个开始向前切片'''
print(lst[::-1])
'''star为7，stop省略，step为-1'''
print(lst[7::-1])
'''start=6,stop=0,step=-2'''
print(lst[6:0:-2])
