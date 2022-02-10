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
    print('            8.退出                      ')
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
    pass


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
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()
