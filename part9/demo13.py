# -*- coding: utf-8 -*-
# @Time : 2022/1/9 4:13
# @Author : jony wang
# @File : demo13.py
'''{}格式化字符串时，指定'宽度和精度'''
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # 这里的.3表示一共是3位数
print('{0:.3f}'.format(3.1415926))  # 如果想保留后3位的话，用.3f这种格式

print('{0:10.3f}'.format(3.1415926))  # 指定宽度为10，精度为3
print('hellohello')  # 这里表示10个位置，宽度为10
