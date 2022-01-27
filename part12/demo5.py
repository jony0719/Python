# -*- coding: utf-8 -*-
# @Time : 2022/1/22 0:55
# @Author : jony wang
# @File : demo1.py
class Student:  # Student为类的名称（类名），由一个或者多个单词组成，每个单词的首字母大写，其余小写。
    native_place = '湖北'  # 直接写在类里的变量，称为类属性

    # 初始化方法
    def __init__(self, name, age):  # 其中带了self，后边可以继续写其他参数。name、age是局部变量
        self.name = name  # 把局部变量name赋值给了实例属性self.name
        self.age = age  # self.age称为实例属性，进行了赋值操作。将局部变量赋值给了实例属性。

    # 实例方法，定义在类里的函数叫做实例方法。相当于函数，不同的是，函数名后的()里是self。
    # 在类里边定义的叫做实例方法，在类之外定义的叫做函数。
    def eat(self):
        print('学生在吃饭。。。')

    # 静态方法
    @staticmethod
    def method():  # 在静态方法中是不允许写self的。
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    # 使用classmethod进行修饰的类方法
    @classmethod
    def cm(cls):  # 类方法要求传入cls参数(client)
        print('我使用了classmethod进行修饰，所以我是类方法')


# 类属性的使用方式
# print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 33)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '澳门'
print(stu1.native_place)
print(stu2.native_place)

print('==============类方法的使用方式=====================')
Student.cm()
print('==============静态方法的使用方式===================')
Student.method()
