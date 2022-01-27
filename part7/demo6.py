# -*- coding: utf-8 -*-
# @Time : 2021/12/28 1:09
# @Author : jony wang
# @File : demo6.py
d = {'name': '张三', 'name': '李四'}  # key不允许重复，否则会覆盖
print(d)
d = {'name': '张三', 'nikename': '张三'}  # value值是可以重复的
print(d)

'''在列表中插入数据'''
lst = [10, 20, 30]
lst.insert(1, 100)  # 在索引为1的位置插入100
print(lst)
