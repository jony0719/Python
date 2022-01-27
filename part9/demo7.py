# -*- coding: utf-8 -*-
# @Time : 2022/1/9 1:02
# @Author : jony wang
# @File : demo7.py
s = 'hello,python'
print('1、', s.isidentifier())  # 不是合法的标识符，合法的标识符是由字母数字下划线组成的
print('2、', 'hello'.isidentifier())  # hello是合法的标识符
print('3、', '张三_'.isidentifier())  # 是合法的标识符
print('4、', '张三_123'.isidentifier())

print('5、', '\t'.isspace())  # 判断指定字符串是否由空白字符串组成

print('6、', 'abc'.isalpha())  # 判断字符串是否全部由字母组成
print('7、', '张三'.isalpha())
print('8、', '张三1'.isalpha())  # 张三1，不是全部由字母组成

print('9、', '123'.isdecimal())  # 判断字符串是否全部由十进制数字组成
print('10、', '123四'.isdecimal())  # 123四,不是全部十进制数
print('11、', 'ⅠⅡⅢ'.isdecimal())  # 罗马数字，不是十进制数

print('12、', '123'.isnumeric())  # 123，是全部由数字组成
print('13、', '123四'.isnumeric())
print('14、', 'ⅠⅡⅢ'.isnumeric())  # 罗马数字也是数字

print('15、', 'abc1'.isalnum())  # 判断是否全部由数字和字母组成
print('16、', '张三123'.isalnum())  # 张三123,是由数字和字母组成
print('17、', 'abc!'.isalnum())  # !不属于数字或者字母
