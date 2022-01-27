# -*- coding: utf-8 -*-
# @Time : 2021/12/26 1:09
# @Author : jony wang
# @File : demobreak3.py
'''流程控制语句break与continue在二层循环中的使用'''
'''代表外层重复执行5次'''
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j)
'''
当内层循环为break的时候，实际上内层循环执行1次，第二的时候就跳出内层循环了。
当内层训话为continue的时候，当j是偶数的时候，跳出当前循环，继续下一次的循环;
当j是基数的时候，打印j。所以内层循环打印的是1-10的基数。
'''

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
