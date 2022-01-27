# -*- coding: utf-8 -*-
# @Time : 2022/1/22 0:55
# @Author : jony wang
# @File : demo1.py
class Student:  # Student为类的名称（类名），由一个或者多个单词组成，每个单词的首字母大写，其余小写。
    pass


# python中一切皆对象,Student是对象吗？内存中有开空间吗？
print(Student)  # <class '__main__.Student'>
print(id(Student))  # 2998456817728
print(type(Student))  # <class 'type'>
