# -*- coding: utf-8 -*-
# @Time : 2022/1/27 0:16
# @Author : jony wang
# @File : demo11.py
import time

import schedule


def job():
    print('哈哈。。。')


# 可以用来定时发送邮件，办公自动化
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)