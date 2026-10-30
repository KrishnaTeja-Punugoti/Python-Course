Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
-l=[1,2,3,4,5]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?




l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l.pop()
5
l.pop()
4
l
[1, 2, 3]


l=[1,2,3,4,5]

l
[1, 2, 3, 4, 5]

del 1[2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del 1[2]
TypeError: 'int' object does not support item deletion
del 1[2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del 1[2]
TypeError: 'int' object does not support item deletion


del l[2]
d
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?




l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
del l[2]
l
[1, 2, 4, 5]
del l[0]
l
[2, 4, 5]


l
[2, 4, 5]
l.clear()
l
[]




l=[1,2,3,4,5,6,7,8,9,10]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.count()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)


l=[1,2,3,4,5,6,7,8,9,10]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.count(8)
1
l.count(9)
1
l=[1,2,3,4,5,6,7,8,9,1,34,7,2,8,8,9,4,5,5,6,2,7,0]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 34, 7, 2, 8, 8, 9, 4, 5, 5, 6, 2, 7, 0]
l.count(5)
3

l.index(5)
4
sorted(1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
sorted(5)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sorted(5)
TypeError: 'int' object is not iterable
sorted(l)
[0, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 34]
l.reverse()
l
[0, 7, 2, 6, 5, 5, 4, 9, 8, 8, 2, 7, 34, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l.sort(reverse=True)
l
[34, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 2, 2, 2, 1, 1, 0]

a=[1,2]
c=a
c
[1, 2]
a is c
True
 c.append(3)
 
SyntaxError: unexpected indent
c.append(3)
c
[1, 2, 3]
a.append(3)
c
[1, 2, 3, 3]
b=a.copy()
b
[1, 2, 3, 3]
b.append(30)
b
[1, 2, 3, 3, 30]
a
[1, 2, 3, 3]




l
[34, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 2, 2, 2, 1, 1, 0]
any(l)
True
l.append(0)
l
[34, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 2, 2, 2, 1, 1, 0, 0]
any(l)
True
all(l)
False
k=[0,0.0,'']
any(k)
False
all(k)
False
all(l)
False
all(k)
False


l
[34, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 2, 2, 2, 1, 1, 0, 0]
sum(l)
143


t=()
t=tuple()
t=(1,2,3)
t=tuple((1,2,3,4,5))
t
(1, 2, 3, 4, 5)
type(t)
<class 'tuple'>
t=1,2,3,4,5,6,7
t
(1, 2, 3, 4, 5, 6, 7)
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,2,3,4,5,1,5,5)
t
(1, 2, 3, 4, 5, 1, 5, 5)
t=(1,1.2,'teja',[1,2,3,4,5],{1,2,3},{1,2},{1,1},False)
t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
t=(1,2,3,4,5)
a,b,c,d,e=t
a
1
b
2
c
3
d
4
e
5


len(t)
5
t[3].append(1)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    t[3].append(1)
AttributeError: 'int' object has no attribute 'append'
t[3].append(1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    t[3].append(1)
AttributeError: 'int' object has no attribute 'append'


t
(1, 2, 3, 4, 5)
t[3].append(1)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    t[3].append(1)
AttributeError: 'int' object has no attribute 'append'

t
(1, 2, 3, 4, 5)
t=(1,2,3)
t
(1, 2, 3)
t[3]
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    t[3]
IndexError: tuple index out of range
t[3]=(1,2,3)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    t[3]=(1,2,3)
TypeError: 'tuple' object does not support item assignment




t.append(1)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
t.append()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    t.append()
AttributeError: 'tuple' object has no attribute 'append'




a=(1,2,3,4,5)
b=(6,7,8,9,10)

t
(1, 2, 3)
a
(1, 2, 3, 4, 5)
b
(6, 7, 8, 9, 10)

a+b
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
a
(1, 2, 3, 4, 5)
t=(1,1.2,'teja',[1,2,3,4,5],{1,2,3},{1,2},{1,1},False)
t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
t[2]
'teja'
t[-1]
False
t[4]
{1, 2, 3}
t[3:6]
([1, 2, 3, 4, 5], {1, 2, 3}, {1, 2})
t[::-1]
(False, {1}, {1, 2}, {1, 2, 3}, [1, 2, 3, 4, 5], 'teja', 1.2, 1)
t[-2:]
({1}, False)
t[-4:]
({1, 2, 3}, {1, 2}, {1}, False)
t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
l in t
False
10 not in t
True
False not in t
False


t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
len(t)
8
sorted(t)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
max(t)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'


t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
max(t)
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'


t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
type(t)
<class 'tuple'>
KeyboardInterrupt
t
(1, 1.2, 'teja', [1, 2, 3, 4, 5], {1, 2, 3}, {1, 2}, {1}, False)
len(t)
8
sorted(t)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'



t=(1,2,3,4,5,6,7,8,9,10)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
len(t)
10
max(t)
10
min(t)
1
sorted(t)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t.count(2)
1
t.index(8)
7
any(t)
True
all(t)
True
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum(t)
55




s={90.6,55,18,1,5,99}
s
{1, 18, 99, 5, 55, 90.6}
s={1,1,1,1,1,1,1}
s
{1}
s={90.6,55,18,1,5,99}
s
{1, 18, 99, 5, 55, 90.6}
s.add(1.2)
s
{1, 18, 99, 1.2, 5, 55, 90.6}
s.add("str")
s
{1, 18, 99, 1.2, 5, 55, 'str', 90.6}
s.add(2+3j)
a
(1, 2, 3, 4, 5)
s
{1, 1.2, 5, 'str', (2+3j), 18, 90.6, 99, 55}
a={1,4,6,8}
b={4,5,6,7,8,9}

>>> 4 in a
True
>>> 7 is not in a
SyntaxError: invalid syntax
>>> 7 not in a
True
>>> 
>>> a
{8, 1, 4, 6}
>>> b
{4, 5, 6, 7, 8, 9}
>>> a|b
{1, 4, 5, 6, 7, 8, 9}
>>> a^b
{1, 5, 7, 9}
>>> a7b
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    a7b
NameError: name 'a7b' is not defined
>>> a&b
{8, 4, 6}
>>> a
{8, 1, 4, 6}
>>> b
{4, 5, 6, 7, 8, 9}
>>> a-b
{1}
>>> a
{8, 1, 4, 6}
>>> b
{4, 5, 6, 7, 8, 9}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({99,100})
True
>>> a
{8, 1, 4, 6}
>>> {8}.issubset(a)
True
>>> {100,99}.issubset(a)
False
>>> a.issubset(b)
False
>>> {1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True
