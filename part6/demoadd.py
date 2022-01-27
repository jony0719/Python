# -*- coding: utf-8 -*-
# @Time : 2021/12/26 22:59
# @Author : jony wang
# @File : demoadd.py
'''append()方法，在列表末尾添加一个元素'''
lst = [10, 20, 30]
print('添加之前:', lst, id(lst))
lst.append(40)
print('添加之后:', lst, id(lst))
'''问题：有没有创建新的列表对象？只需要看下列表对象的id是否一样，一样的话未创建新的列表对象'''

'''使用extend()方法，在列表末尾添加至少一个元素'''
lst2 = ['hello', 'world']
# lst.append(lst2)  # 将lst2作为一个元素，添加到列表的末尾
lst.extend(lst2)  # 将lst列表的末尾依次添加多个元素
print(lst)

'''使用insert()方法，在列表的任意位置添加一个元素'''
'''此时的lst=[10,20,30,40,'hello','world']，在lst索引为1的位置添加66'''
lst.insert(1, 66)
print(lst)

'''切片，在列表的任意位置添加至少一个元素'''
'''此时的lst=[10, 66, 20, 30, 40, 'hello', 'world']'''
lst3 = ['True', 'False', 'hello']
lst[1:] = lst3
print(lst)
'''
注意：切片实际上，相当于将后边的切掉，把切掉的部分用新的列表替换。
'''
