# -*- coding: utf-8 -*-
# @Time : 2021/11/28 22:24
# @Author : jony wang
# @File : add.py

# 转义字符
print('hello\nworld')  # \ +转义功能的首字母 n->newline的首字母表示换行
print('helloworld')

print('hello\tworld')
print('helloooo\tworld')

print('hello\rworld')  # 当输出完hello后，回到行首输出world将hello给覆盖掉了，所以输出会是world

print('hello\bworld')  # \b 表示退格

print('https:\\www.baidu.com')
print('https:\\\\www.baidu.com')
# print('老师说：‘大家好’‘)
# 在输出的内容中保留单引号，需要在前面加上转义字符
print('老师说:\’大家好\‘')

# 原字符，希望字符串中的转义字符不起作用，或使用原字符，就是在字符串前加上r或者R
print('hello\nworld')
print(r'hello\nworld')
# 注意，字符串最后一个字符不能是\，否则会出现报错.但是两个\\是允许的
# print(r'helloworld\')    这里会出现报错
# print(r'hello\nworld\\') 两个\\是允许的
