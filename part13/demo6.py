# -*- coding: utf-8 -*-
# @Time : 2022/1/23 22:43
# @Author : jony wang
# @File : demo6.py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 22)
print(dir(stu))  # 查看stu对象的属性和方法，这些属性和方法不是在Student类中定义的，是在object类中继承过来的

# object的__str__()方法，用于返回对象的描述
print(stu)  # 一旦重写str后，不再返回对象的内存地址而是调用 __str__()输出的内容
print(type(stu))

'''
总结：经常在写完初始化方法后，会去重写它的__str__()方法，用于返回对象的描述
'''