#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-


#列表重构
liebiao=[[1,2,3],[4,5],[6],[7,8,9]]
a=sum(liebiao,[])
#或者
from functools import reduce
from operator import add
data = [[1,2,3],[4,5],[6],[7,8,9]]
reduce(add, data)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#字典生成

{a:a**2 for a in range(1,10)}
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#类中方法重置
class foo:
    def normal_call(self):
        print ('normal_call')
    def call(self):
        print ('first_call')
        self.call=self.normal_call
y = foo()
y.call()
# first_call
y.call()
# normal_call
y.call()
# normal_call

#获取类属性

class GetAttr(object):
    def __getattribute__(self, name):
        f=lambda:'Hello {}'.format(name)
        return f

g=GetAttr()
g.Mark()
# 'Hello Mark'

#集合
a=set([1,2,3,4])
b=set([3,4,5,6])
a|b
#{1, 2, 3, 4, 5, 6}
a&b
#{3, 4}
a^b
#{1, 2, 5, 6}
set([1, 2, 3]) == {1, 2, 3}
set((i*2 for i in range(10))) == {i*2 for i in range(10)}

#错误的默认值导致错误
def foo(x=[]):
    x.append(1)
    print x

#默认值设置为无
def foo(x=None):
   if x is None:
       x = []
       x.append(1)
   print x
foo()
# [1]
foo()
# [1]

sdfasdfas=234