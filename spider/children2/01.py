'''正则表达式'''

import re

'''Match使用案例'''
#以下正则分为两个小组，以小括号为单位
s = r'([a-z]+) ([a-z]+)'#r表示后面字符不需要转义

pattern = re.compile(s,re.I)#re.I表示忽略大小写
m = pattern.match('Hello world wide web')

#group(0)表示返回成功匹配的整个字串
s = m.group(0)
print(s)

#返回成功匹配的整个字串的跨度
a = m.span(0)
print(a)

s = m.group(1)
print(s)

a = m.span(1)
print(a)

#等价于m.group(1) m.group(2)
s = m.groups()
print(s)

print('*'*20)
'''search使用案例'''
s = r'\d+'
pattern = re.compile(s)
m = pattern.search('one12two34three56')
print(m)

m = pattern.search('one12two34three56',10,40)
print(m)

print('*'*20)
'''findall返回列表,finditer返回迭代器 使用案例'''
pattern = re.compile(r'\d+')
m = pattern.findall('I am 18 years old and I love shating,she 18')
print(m)

m = pattern.finditer('I am 18 years old and I love shating,she 18')
for i in m:
    print(i)

print('*'*20)
'''中文unicode案例'''
pattern = re.compile(r'[\u4e00-\u9fa5]+')
m = pattern.findall(u'我 爱 篮球')
print(m)

