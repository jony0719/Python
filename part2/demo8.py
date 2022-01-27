# -*- coding: utf-8 -*-
# @Time : 2021/12/18 2:26
# @Author : jony wang
# @File : demo8.py
name = '张三'
age = 18
print(type(name), type(age))  # 说明name和age的数据类型不一致
# print('我叫'+name+'今年'+age+'岁')  #当str类型与int类型进行拼接的时候，会报错。解决方案将int类型转换为str类型。
print('我叫' + name + '今年，' + str(age) + '岁')  # 将int类型通过str()函数转换为str类型

print('==========使用str()函数，将其他类型转换为str类型========')
a = 10  # 整数型
b = 20.99  # 浮点型
c = True  # 布尔型
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

print('=======int()函数，将其他类型转换为int类型==============')
s1 = '123'
s2 = 99.8
s3 = '3.1415'
s4 = True
s5 = 'hello'
print('原有数据类型：', type(s1), type(s2), type(s3), type(s4), type(s5))  # 原有的数据类型

print(int(s1), type(int(s1)))  # 将str型转换为int类，字符串为数字串
print(int(s2), type(int(s2)))  # 将float型转换为int，小数部分抹零
# print(int(s3),type(int(s3)))     小数类型字符串，无法转换为整数
print(int(s4), type(int(s4)))
# print(int(s5),type(int(s5)))     文字类型字符串，无法转换为整数。将字符串转换为int型，必须是数字串且为整型数字串。

# print(int(s1),int(s2),int(s3),int(s4),int(s5),type(int(s1)),type(int(s2)),type(int(s3)),type(int(s4)),type(int(s5)))
print(int(s1), int(s2), int(s4), type(int(s1)), type(int(s2)), type(int(s4)), )

print('========使用float()，将其他数据类型转换为float类型===========')
s1 = '123.98'
s2 = '99'
s3 = True
s4 = 'hello'
s5 = 98
print('原有的数据类型:', type(s1), type(s2), type(s3), type(s4), type(s5))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(s3), type(float(s3)))
# print(float(s4),type(float(s4)))   文字类型字符串，无法转换为浮点数；非数字串无法转换为float类型
print(float(s5), type(float(s5)))
