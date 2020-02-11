#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:31:49 2019

@author: meixiangui
"""

import datetime as dt
import time as tm

tm.time()
# timestamp format of date 

dtnow = dt.datetime.fromtimestamp(tm.time())
# transform to date format 
dtnow 

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

# delta
delta = dt.timedelta(days = 100)
delta 

today = dt.date.today()
today - delta

today > today - delta

# map in python 
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title,lastname)

list(map(split_title_and_name, people))

# lambda in python 
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

# lambda is a simple function, map is "apply' to a list 


#list comprehensions 

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]

#numpy 
import numpy as np
m = np.array([[7,8,9],[10,11,12]])
m 
m.shape
n = np.arange(0,30,2)
n
n = n.reshape(3,5)
n

o = np.linspace(0,4,9)
o 
o.resize(3,3)
o

np.ones((3,2))
np.zeros((2,3))
np.eye(3)
y = np.array([6,7,8])
np.diag(y)
np.array([1,2,3] * 3)

np.repeat([1,2,3], 3)
p = np.ones([2,3], int)
p 
# row bind - vstack
np.vstack([p,2*p])
np.hstack([p,2*p])

# numpy operations 
x = np.array([1,2,3])
x.dot(y)
np.dot(x,y)
sum(x*y)

z = np.array([y, y**2])
z.shape
z.T
z.T.shape

z.dtype
z = z.astype("f")
z.dtype

# find index of a max or min value
a = np.array([-4,-2,1,3,5])
a.argmax()
a.argmin()
 
# indexing / slicing 
s = np.arange(13)**2
s 
s[0], s[4], s[0:3]
s[1:5]
s[-4:]
s[-5::-2] # from -5 position, selct every 2 elements 

r = np.arange(36)
r.resize((6,6))
r
r[:2, :-1] # first 2 rows, all the columns except for the last 
r[-1,::2]

r2 = r[:3,:3]
r2
r2[:] = 0
r
# r will also be changed 

r_copy = r.copy()
r_copy[:] = 10 
r
# r will not changed 

test = np.random.randint(0,10,(4,3))
test

for i, row in enumerate(test):
    print('row', i, 'is', row)

test2 = test**2
test2 
for i, j in zip(test, test2):
    print(i, '+', j, '=', i+j)


r = np.arange(36)
r = r.reshape(6,6)
r[0:6,::-7]
r[::7] # you are jumping for every row list
r.reshape(36)[::7]
r[:,::7]
r[2:4,2:4]
















