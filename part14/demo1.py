# -*- coding: utf-8 -*-
# @Time : 2022/1/26 19:43
# @Author : jony wang
# @File : demo1.py
def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '湖北'

    def eat(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 10
b = 20
print(a + b)
