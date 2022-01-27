# -*- coding: utf-8 -*-
# @Time : 2021/12/27 0:28
# @Author : jony wang
# @File : demoremove.py
'''使用remove()方法，删除列表元素'''
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)  # 从列表移除一个元素，重复元素只删除第一个。
print(lst)
# lst.remove(90)  # 移除的列表元素不存在，就抛出ValueError

'''使用pop()方法，删除一个指定索引位置上的元素'''
print('此时lst列表为:', lst)
lst.pop(1)  # 删除索引位置为1上的元素
print(lst)
# lst.pop(5)  # 移除索引位置为5(索引为5不存在)上的元素,抛出indexError
lst.pop()  # 不指定索引，默认删除列表中最后一个元素
print(lst)

'''使用切片，一次至少删除一个元素；注意切片会产生新的列表'''
new_list = lst[1:3]
print('原列表:', lst)
print('切片后的列表:', new_list)

'''如何删除列表中的元素，而不产生新的列表对象？'''
print('原列表为:', lst)
lst[1:3] = []  # 使用空列表去代替
print('切片后的列表:', lst)

'''使用clear()清空列表'''
print('原列表为:', lst)
lst.clear()
print('清空后的列表:', lst)

'''使用del删除列表对象'''
# del lst
# print(lst)  # 程序抛出错误，列表对象未定义
