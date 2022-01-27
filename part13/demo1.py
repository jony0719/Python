# -*- coding: utf-8 -*-
# @Time : 2022/1/23 21:21
# @Author : jony wang
# @File : demo1.py
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动。。。')


car = Car('宝马X5')
car.start()
print(car.brand)
