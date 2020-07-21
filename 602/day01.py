'''
from functools import *
print(reduce(lambda x,y:x+y,[1,2,3]))
'''
'''
amount = 0

d = float(input('请输入货物吨数d：'))

s = float(input('请输入运输距离s:'))

def compute(d,s):
    p1,p2,p3,p4,p5,p6 = 10,8,7,6,5.5,5
    if s<100:
        amount = p1*d
    elif s<150:
        amount = p2*d
    elif s<200:
        amount = p3*d
    elif s<300:
        amount = p4*d
    elif s<500:
        amount = p5*d
    else:
        amount =p6*d

    if amount>5000:
        amount *= 0.95

    print('应付的实际运费额为:{0}{1}'.format(amount,'元'))

compute(d,s)
'''


'''
days =0
year = int(input('year:'))
month = int(input('month:'))
months = (31,28,31,30,31,30,31,31,30,31,30,31)

#考虑如果是闰年的情况
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if 0 < month <= 12:
    days = months[month - 1]
#如果是闰年并且等于2月要多加一天
if (leap == 1) and (month == 2):
    days = 29

print(days)
'''

s = input('请输入字符串：')
upper = 0
lower = 0
digit = 0
el = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        el += 1

print('大写字母个数为{},小写字母个数为{},数字个数为{},其它字符个数为{}'.format(upper,lower,digit,el))


'''
num = []
num_len = 0
for i in range(100):
    if i > 1:
        temp = 0
        for j in num:
            if i % j == 0:
                temp += 1
        if temp == 0:
            num_len += 1
            num.append(i)
pr1int(num)
'''