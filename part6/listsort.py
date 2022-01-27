# -*- coding: utf-8 -*-
# @Time : 2021/12/27 1:09
# @Author : jony wang
# @File : listsort.py
lst = [20, 40, 10, 98, 54]
'''调用sort(）方法进行排序'''
print('排序前的列表为:', lst, id(lst))
lst.sort()
print('从小到大排序后的列表为:', lst, id(lst))  # 默认从小到大的顺序进行排序
lst.sort(reverse=True)  # 指定reverse=True)，按照从大到小就那些排序
print('从大到小排序后的列表为:', lst, id(lst))

'''调用内置函数sorted()函数进行排序,将产生一个新的列表'''
print('排序前的的列表:', lst, id(lst))
new_list = sorted(lst)
print('排序后的列表为:', new_list, id(new_list))  # 升序排序
new_list2 = sorted(lst, reverse=True)  # 指定reverse=True进行降序排序
print('排序后的列表为:', new_list2, id(new_list2))

'''原列表的id与新列队的id不同，产生了新的列表'''
