# -*- coding: utf-8 -*-
# @Time : 2021/12/28 0:26
# @Author : jony wang
# @File : demo3.py
'''键的判断'''
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

'''字典元素的删除'''
del scores['张三']  # 删除指定的key-value
print(scores)
# scores.clear()  # 清空字典元素
print(scores)

'''字典元素的新增'''
print('新增前的字典元素:', scores)
scores['陈六'] = 99
print('新增后的字典元素:', scores)

'''字典元素的修改'''
print('修改前的字典元素:', scores)
scores['陈六'] = 97
print('修改后的字典元素:', scores)
