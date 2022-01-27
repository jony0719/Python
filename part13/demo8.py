# -*- coding: utf-8 -*-
# @Time : 2022/1/24 0:27
# @Author : jony wang
# @File : demo8.py
# dir()方法查看对象的属性和方法
# print(dir(object))  # 查看object类对象的属性和方法
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 创建C类对象
x = C('Rose', 20)  # C类的实例对象

print(x.__dict__)  # 查看实例对象绑定了哪些属性和方法
print(C.__dict__)  # 查看类对象绑定了哪些属性和方法
print('============================')
print(x.__class__)  # <class '__main__.C'>,输出对象所属的类
print(C.__bases__)  # 输出C类的父类类型的元素
print(C.__base__)  # 输出的是最近的父类。谁最近先输出谁
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 查看A的子类.由C和D.子类的列表
