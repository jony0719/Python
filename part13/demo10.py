# -*- coding: utf-8 -*-
# @Time : 2022/1/24 23:46
# @Author : jony wang
# @File : demo10.py
class Person(object):
    def __new__(cls, *args, **kwargs):  # 用于创建对象
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)  # Person继承了object类，调用object类的__new__，并传入cls
        print('创建对象的id为:{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):  # 用于初始化对象
        print('__init__被调用了,self的id值为:{0}'.format(id(self)))
        self.name = name  # name与age是实例对象
        self.age = age


print('obj这个类对象的id为:{0}'.format(id(object)))
print('Person类对象的id为:{0}'.format(id(Person)))

# 创建Person类的实例对象
p1 = Person('张三', 20)
print('p1这个Person类的实例对象的id为:{0}'.format(id(p1)))
