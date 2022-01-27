# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:48
# @Author : jony wang
# @File : demo9.py
def fun(a, b):
    c = a + b  # c称为局部变量，因为c在函数体内进行定义的变量，a,b称为函数的形参，相当于局部变量
    print(c)


# print(a)  因为a和c超出了起作用的范围（超出了作用域），所以程序报错
# print(c)
name = '杨老师'  # name的作用范围为函数内部和外部都可以使用。称为全局变量


def fun2():
    print(name)


fun2()  # 调用函数


def fun3():
    global age  # 函数内部定义的变量，局部变量。局部变量使用global声明，这个变量实际上就变成全局变量
    age = 20
    print(age)


fun3()
print(age)
