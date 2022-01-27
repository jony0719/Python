# -*- coding: utf-8 -*-
# @Time : 2022/1/23 21:28
# @Author : jony wang
# @File : demo2.py
class Student():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个_

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 22)
stu.show()

# 在外部使用name和age
print(stu.name)
# print(stu.__age)  # 不允许在类的外部使用

# 如何在类的外部使用
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问
