# -*- coding: utf-8 -*-
# @Time : 2022/1/9 0:02
# @Author : jony wang
# @File : demo5.py
s = 'hello,Python'

'''居中对齐'''
print(s.center(20, '*'))

'''左对齐'''
print(s.ljust(20, '*'))
print(s.ljust(10, '*'))  # 如果设置的宽度小于实际宽度，则返回原字符
print(s.ljust(20))  # 如果第二个参数不写，默认是空格。

'''右对齐'''
print(s.rjust(20, '*'))
print(s.rjust(20))  # 如果第二个参数不写，默认是空格。
print(s.rjust(10))  # 如果设置的宽度小于实际宽度，则返回原字符

'''右对齐，用0进行填充'''
print(s.zfill(20))  # 左边用0填充
print(s.zfill(10))  # 如果设置的宽度小于实际宽度，则返回原字符
print('-8910'.zfill(8))
'''
注意：
-8910加上-号是5位，所以会在减号后补充3个0
'''
