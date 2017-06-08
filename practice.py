#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'hello world', 'i am', 'maomao'
# name = raw_input('plrase input your name: ')
# print 'hello', name
stra = 'i\'m \"nidaye\"'
print stra
print 'i\'m leaning\npython'
print '\\\n\\'
print r'\\\n\\'
print r'''\n\tline1
line2
line3'''

print not False
PI = 3.1415926
PI = 3.14
print PI

print ord('a')
print chr(65)
print u'中文'

t = (1,)
print t
t = (1, [2, 3])
print t
for m in t:
    print m

print range(10, 100, 9)

'''birth = int(raw_input('请输入你的出生年份'))
if birth > 2000:
    print '00后'
else:
    print '00前'
'''
dict = {'maomao': 95, 'gouzi': 59}
print dict['maomao']
print 'maomao' in dict
print dict.get('maomi', -1)
print dict.pop('maomao')
# print dict['maomao']
dict['maomao'] = 97
print dict
dict['a'] = 90
print dict

#key = [1, 2, 3]
#dict[key] = 'a list'
s = set([1, 2, 3, 4, 4])
print s
b = set([2, 3, 4, 5, 6])
print s & b
print s | b
# s = set([t])
print s

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
i = power(5)
print i

def add_end(L = None):
    if L is None:
        L =[]
    L.append('end')
    return L

print add_end()
print add_end()
print add_end()

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print calc(*nums)

def person(name, age, **kw):
    return 'name: ', name, 'age: ',age,'other', kw
print person('meimao', 17, city ='taixing',lover = 'gouzi')
kw = {'city': 'taixng', 'lover' : 'maomao'}
print person('gouzi', 38, **kw)

def func(a, b, c=0, *args, **kw):
    return 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
print func(1, 2, 3, 'a', 'b', x=99)

def fact(n):
    if n ==1:
        return 1
    return n * fact(n - 1)
print fact(5)

