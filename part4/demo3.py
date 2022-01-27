# -*- coding: utf-8 -*-
# @Time : 2021/12/23 0:15
# @Author : jony wang
# @File : demo3.py

'''会员，会员消费金额大于200打8折；消费金额大于200小于100打9折;小于100不打折。
非会员，只有消费在200以上打9.5折;小于200不打折。'''
'''n1=input('是否为会员？')
n2=int(input('请输入消费金额：'))
if n1=='y' or n1=='Y':
    if n2>=200:
        print('打8折，打完折后：'+str(n2*0.8))
    elif 100<=n2<200:
        print('打9折，打完折后：'+str(n2*0.9))
    elif 0<=n2<100:
        print('消费金额小于100不打折，消费金额为：'+str(n2))
 else:
     print('请输入合法的消费金额！')

else:
    if n2>=200:
        print('打9.5折，打完折后：'+str(n2*0.95))
    elif 0<=n2<200:
        print('非会员，消费金额小于200不打折，消费金额为：'+str(n2))
    else:
        print('请输入合法的消费金额！')
'''

answer = input('您是会员吗？Y/y:')
money = float(input('请输入您的消费金额：'))
if answer == 'Y' or answer == 'y':
    if money >= 200:
        print('打8折，付款消费：', money * 0.8)
    elif 100 <= money < 200:
        print('打9折，付款消费：', money * 0.9)
    elif 0 <= money < 100:
        print('不打折，付款金额：', money)
    else:
        print('请输入合法的消费金额！')
else:
    if money >= 200:
        print('打95折，付款金额：', money * 0.95)
    elif 0 <= money < 200:
        print('不打折，付款金额：', money)
    else:
        print('请输入合法的消费金额！')
