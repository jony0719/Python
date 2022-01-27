# -*- coding: utf-8 -*-
# @Time : 2022/1/25 23:09
# @Author : jony wang
# @File : demo11.py
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# (2)变量的赋值
cpu1 = CPU()  # 创建一个CPU类的对象
cpu2 = cpu1  # 变量的赋值
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))

# （2）类的浅拷贝与深拷贝
print('=============================================')
disk = Disk()  # 创建一个硬盘类的对象
computer = Computer(cpu1, disk)  # 创建一个计算机类的对象

# 浅拷贝
import copy

print(disk)

computer2 = copy.copy(computer)  # 浅拷贝
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

print('==============================================')
# 深拷贝
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
