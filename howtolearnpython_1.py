# -*- encoding=UTF-8 -*-

# print 1j * 1J
# print 1j * complex(0,1)
# print 1j * complex('1+2j')
# a = 4.0 + 3.0j
# print a.real
# print a.imag
# print abs(a)
# print 'doesn\'t'
# print 'I\'m a girl.\n\t'
# print 1
# print 'He says"Yes,I love\'t you"'
# print '"Isn\'t," she said.'
# print "'maomao',i love you"
# hello = "This is a rather long string containing\n\
# several lines of text just as you would do in C.\n\
#     Note that whitespace at the beginning of the line is\
#  significant.\n"
#
# print hello
#
# print """\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """
# print r"This is a rather long string containing\n\
# several lines of text much as you would do in C."
# word = 'Helpme'
# print word
# print '<' + word * 5 + '>'
# print 'str''ing'
# print '12345str'.strip('213') + 'ing'
# print word.split('m')
# print word[4]
# print word[0:2]
# print word[2:4]
# print word[::-1]
# print 1 , word[-1]
# print 2 , word[:-3]
# print 3 , word[:-3:-1]
# word = 'www.google.com'
# print word
# print word.split('.')[:-1]
# print word[:2] +' ' + word[2:]
# print word[2:1]
# word = 'Helpme'
# print word[-1]
# print word[-3]
# a = ['spam', 'eggs', 100, 1234]
# print a[:2] + ['bacon', 2*2]
# print 3*a[:3]+['Boo!']
# a[0:2] = [1,12]
# print 1, a
# a[0:2]=[]
# print 2, a
# a[1:1] =['bletch', 'xyzzy']
# print 3, a
# a[1:2] =['bletch', 'xyzzy']
# print 4, a
# a[:] = []
# print a
# a = ['a', 'b', 'c', 'd']
# print len(a)
# q = [2,3]
# p =[1, q, 4]
# print len(p)
# print p[1]
# print p[1][0]
# p[1].append('xtra')
# print p
# print q

# a, b = 0, 1
# while b < 1000:
#     print b,
#     a, b = b, a + b

# x = int(raw_input('请输入一个数：'))
# if x < 0:
#     x = 0
#     print 'x<0'
# elif x == 0:
#     print '0'
# elif x == 1:
#     print 1
# else:
#     print 'more'

# a = range(0,16)
# for x in a[:]:
#     print x,
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print i,a[i]

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print 'n=', n
#             print 'x=', x
#             print 'n % x= ', n % x
#             print n, '=', x, '*', n/x
#             break
#     else:
#         print n, '是素数'

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print a,
#         a, b = b, a+b
# # Now call the function we just defined:
# fib(2000)
# f = fib
# f(100)

i = 5
def f(arg=i):
    print arg
#
# i=6
# f()
#
# def f(a, l=[]):
#     l.append(a)
#     return l
# print f(1)
# print f(2)
# print f(3)
#
# def f(a, l=None):
#     if l is None:
#         l = []
#     l.append(a)
#     return l
# print f(1)
# print f(2)
# print f(3)

# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print f(0)
# print f(1)


# i = 0
# while i < 5:
#     try:
#         ++i
#         print 1
#     except ZeroDivisionError:
#         print '除数不为零'

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise