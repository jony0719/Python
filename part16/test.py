# -*- coding: utf-8 -*-
# @Time : 2022/2/13 22:04
# @Author : jony wang
# @File : test.py
lst = [{'id': '1001', 'name': '王强', 'english': 111, 'python': 103, 'java': 105},
       {'id': '1002', 'name': '张三', 'english': 111, 'python': 102, 'java': 123},
       {'id': '1003', 'name': '李四', 'english': 121, 'python': 109, 'java': 108}]


def show_student():
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


show_student()
