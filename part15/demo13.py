# -*- coding: utf-8 -*-
# @Time : 2022/1/28 14:51
# @Author : jony wang
# @File : demo13.py
'''
MyContentMgr实现了特殊方法__enter__()和__exit__()，该类对象遵守了上下文管理协议
该类对象的实例对象，称为上下文管理器
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了', 1 / 0)


with MyContentMgr() as file:  # 相当于file=MyContentMgr()
    file.show()

'''
在上下文管理器中，不论是否异常都会调用特殊方法，__exit__()方法自动退出。
'''
