# -*- coding: utf-8 -*-
# @Time : 2022/1/9 20:01
# @Author : jony wang
# @File : demo2.py
'''定义函数fun'''


def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(101)
    print('arg1:', arg1)
    print('arg2', arg2)
    return


'''调用函数fun()'''
n1 = 11
n2 = [22, 33, 44]
print('n1:', n1)
print('n2:', n2)

print('============fun()函数调用===============')
fun(n1, n2)  # 位置传参，arg1,arg2是函数定义处的形参，n1,n2是函数调用处的实参。实参名称可以与形参名称不一致
print('n1:', n1)
print('n2:', n2)

'''
在函数的调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值，arg1的值修改为100，不会影响n1的值
如果是可变对象，在函数体的修改会影响到实参的值 arg2的修改，append(101),会影响到n2的值。
'''
