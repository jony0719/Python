# -*- coding: utf-8 -*-
# @Time : 2021/12/25 2:56
# @Author : jony wang
# @File : demofor2.py
'''输出100-999之间的水仙花数'''
'''
什么是水仙花数？
举例：153=3*3*3+5*5*5+1*1*1
说明：个位数的3次方+十位数的三次方+百位数的三次方和等于某个数
'''
'''a表示百位数，b表示十位数，c表示个位数'''
for item in range(100, 1000):
    a = item // 100
    b = (item - a * 100) // 10
    c = item - a * 100 - b * 10
    if item == a * a * a + b * b * b + c * c * c:
        print('水仙花数为：', item)

'''代码优化'''
'''
个位数只需与10取余
十位数只需整除10，在求余数
百位数只需要整数100
'''
print('============打印100-999之间的水仙花数==========')
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    # print(bai, shi, ge)
    if item == bai ** 3 + shi ** 3 + ge ** 3:
        print('水仙花数为：', item)
