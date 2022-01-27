# -*- coding: utf-8 -*-
# @Time : 2022/1/28 0:44
# @Author : jony wang
# @File : demo10.py
'''
file = open('d.txt', 'a')
file.write('hello')
file.close()
file.write('world')
file.flush()
'''

'''
上述会报错，因为file.close()关掉了，不允许在执行磁盘操作了。
file.flush()之后可以继续写内容，但是file.close()之后，不允许继续写内容
'''
