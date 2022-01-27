# -*- coding: utf-8 -*-
# @Time : 2022/1/19 22:04
# @Author : jony wang
# @File : demo3.py
lst = [
    {'rating': [9.7, 2062397], 'id': 1292052, 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆.罗宾斯', '摩根.弗里曼']},
    {'rating': [9.6, 1528760], 'id': 1291546, 'type': ['剧情', '爱情', '同性'], 'title': '霸王别姬',
     'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
    {'rating': [9.5, 155918], 'id': 1292720, 'type': ['剧情', '爱情'], 'title': '阿甘正传', 'actors': ['汤姆.汉克斯', '罗宾.怀特']}]
'''要求：使用列表存储电影信息，输入名字，在屏幕上显示xxx出演了哪部电影'''
name = input('请输入演员名字：')
for item in lst:  # 首先遍历列表，会得到{}，item是一个字典
    actor_lst = item['actors']  # 得到演员的列表
    # print(actor_lst)  # 会得到演员列表
    for actor in actor_lst:  # 遍历演员列表
        if name in actor:
            print(name + '出演了' + item['title'] + '!')

'''for movie in item:  # 遍历key值，会得到一个个key值，如rating、id
        print(movie)
        print('============这是一个换行====================')
'''
''' actors = movie['actors']
 # print(actors)
 if name in actors:
     print(name + '出演了' + movie)
   '''
