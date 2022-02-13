# -*- coding: utf-8 -*-
# @Time : 2022/2/9 23:28
# @Author : jony wang
# @File : stusystem.py
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请输入您的选择:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您真的要退出系统吗y/Y')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用!!!')
                    break
                else:
                    continue
            if choice == 1:
                insert()
            if choice == 2:
                search()
            if choice == 3:
                delete()
            if choice == 4:
                modify()
            if choice == 5:
                sort()
            if choice == 6:
                total()
            if choice == 7:
                show()


def menu():
    print('=============学生信息管理系统==============')
    print('================菜单选项=================')
    print('            1.录入学生信息                ')
    print('            2.查找学生信息                ')
    print('            3.删除学生信息                ')
    print('            4.修改学生信息                ')
    print('            5.排序                      ')
    print('            6.统计学生总人数              ')
    print('            7.显示所有学生信息            ')
    print('            0.退出                      ')
    print('=======================================')


def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入学生姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的信息保存到字典当中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}

        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break
    # 调用save()函数
    sava(student_list)
    print('学习信息录入完毕!!!')


def sava(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')

    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []  # 定义列表，因为存在同名学生放在列表当中
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):  # 如果文件存在，判断根据id还是姓名查找
            mode = input('1.按ID查找 2.按姓名查找')
            if mode == '1':
                id = input('请输入学生的ID:')
            elif mode == '2':
                name = input('请输入学生的姓名:')
            else:
                print('您输入的有误，请重新输入')
                search()  # 输入有误后，重新查找学生信息
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()  # 读取所有的信息放入student列表中
                for item in student:  # 遍历列表
                    d = dict(eval(item))  # 将字符串转换为字典类型
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)  # 如果id不为空且id查找到，将id到student_query列表当中
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)  # 如果name空，将name到student_query列表中
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break

        else:
            print('暂未保存学生信息！！！')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('学生ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
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


def delete():
    while True:
        student_id = input('请输入需要删除的学生的id:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后重新显示所有学生信息
            answer = input('是否继续删除y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员的ID:')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改学生信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = input('请输入英语成绩:')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except:
                        print('您输入的有误，请重新输入!!!')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否需要修改其他学生信息?y/n')
        if answer == 'y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()  # 将读取到的学生信息保存在列表中
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)

    else:
        return
    asc_or_desc = input('请选择(0.升序 1.降序):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请输入排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序:')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']),
                         reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()  # 将读取到的学生信息放在students列表中
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息。。。')


def show():
    student_lst = []  # 用于保存学生列表的列表
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()  # 将读取到的学生信息放入students中
            for item in students:
                student_lst.append(eval(item))
            if student_lst:  # 当学生列表不为空，显示所有学生信息
                show_student(student_lst)
    else:
        print('暂未保存过数据。。。')


if __name__ == '__main__':
    main()
