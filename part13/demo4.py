# -*- coding: utf-8 -*-
# @Time : 2022/1/23 21:47
# @Author : jony wang
# @File : demo3.py
class Person(object):  # person类继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super(Student, self).__init__(name, age)
        self.stu_num = stu_no

    def info(self):
        super(Student, self).info()
        print(self.stu_num)


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super(Teacher, self).__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super(Teacher, self).info()
        print('教龄:', self.teachofyear)


# 创建学生类对象，以及教师类对象
stu = Student('张三', 20, '001')
teacher = Teacher('李四老师', 43, 10)

# 调用方法
stu.info()
print('============================================================')
teacher.info()
