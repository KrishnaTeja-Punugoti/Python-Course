Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=
SyntaxError: invalid syntax





s=
SyntaxError: invalid syntax





s={1,55,38,9,45,8,18,41,60,88}
s
{1, 38, 8, 9, 41, 45, 18, 55, 88, 60}
sorted(s)
[1, 8, 9, 18, 38, 41, 45, 55, 60, 88]
len(s)
10
max(s)
88
min(s)
1
sum(s)
363
any(s)
True
all(s)
True
s
{1, 38, 8, 9, 41, 45, 18, 55, 88, 60}
s.add(77)
s
{1, 38, 8, 9, 41, 45, 77, 18, 55, 88, 60}
s.add(100)
s
{1, 100, 38, 8, 9, 41, 45, 77, 18, 55, 88, 60}
s.update({10,20,30})
s
{1, 100, 38, 8, 9, 41, 10, 45, 77, 18, 20, 55, 88, 60, 30}

sorted(s)
[1, 8, 9, 10, 18, 20, 30, 38, 41, 45, 55, 60, 77, 88, 100]


s.pop()
1
s.pop()
100\
s.pop()
38
s.remove(41)
s
{8, 9, 10, 45, 77, 18, 20, 55, 88, 60, 30}
s.remove(45)
s
{8, 9, 10, 77, 18, 20, 55, 88, 60, 30}
s.remove(45)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s.remove(45)
KeyError: 45
s.dicard(88)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.dicard(88)
AttributeError: 'set' object has no attribute 'dicard'. Did you mean: 'discard'?
s.discard(88)
s
{8, 9, 10, 77, 18, 20, 55, 60, 30}
s.discard(88)
s.clear()
s
set()


a={1,2,3,4,5}
b={6,7,8,9,10}
a
{1, 2, 3, 4, 5}
b
{6, 7, 8, 9, 10}
c=a.copy()
c.add(20)
c
{1, 2, 3, 4, 5, 20}
a
{1, 2, 3, 4, 5}




d
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?





d={}
d={1:1,2:2}
d
{1: 1, 2: 2}
type(d)
<class 'dict'>
d[]='int'
SyntaxError: invalid syntax
d[1]='int'
d
{1: 'int', 2: 2}
d[1.1]='float'
d
{1: 'int', 2: 2, 1.1: 'float'}

d['str']='com'
s
set()
d
{1: 'int', 2: 2, 1.1: 'float', 'str': 'com'}
d[2+4j]='com'
d
{1: 'int', 2: 2, 1.1: 'float', 'str': 'com', (2+4j): 'com'}
d[(1,2,3)]='tuple'
d
{1: 'int', 2: 2, 1.1: 'float', 'str': 'com', (2+4j): 'com', (1, 2, 3): 'tuple'}
d[False]='bool'
d
{1: 'int', 2: 2, 1.1: 'float', 'str': 'com', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d[[1,2,3,4,5]]='list'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d[[1,2,3,4,5]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[{1,2,3,4,5}]='sst'
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d[{1,2,3,4,5}]='sst'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1,2,3,4,5}]='set'
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d[{1,2,3,4,5}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1.1,2.2,3.3,4.4,5.5}]='dict'
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d[{1.1,2.2,3.3,4.4,5.5}]='dict'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')

d
{1: 'int', 2: 2, 1.1: 'float', 'str': 'com', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}

d[1]=1
d
{1: 1, 2: 2, 1.1: 'float', 'str': 'com', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d.clear()
d
{}


d[1]=1
d[2]=1.2
d[3]=1+2j
d[4]='str'
d[5]=[1,2]
d[6]=(5,6)
d[7]=[{9,8}]
d[8]={3,2}
d[9]={1:1,5:5}
d[10]=False
d[11]=1
d[12]=1
d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 1}

d[12]=2
d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[12]=2

d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}





d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[12]
2
d[10]
False
d[4]
'str'
d[6]
(5, 6)
d[8]
{2, 3}
d[18]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    d[18]
KeyError: 18
d[30]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    d[30]
KeyError: 30
get[18]
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    get[18]
NameError: name 'get' is not defined. Did you mean: 'set'?
d.get[18]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    d.get[18]
TypeError: 'builtin_function_or_method' object is not subscriptable
d.get(18)
d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d.get(7)
[{8, 9}]
d.get(30,'there is no element')
'there is no element'
d.get(5,'there is no element')
[1, 2]





'str' in d
False
1 in d
True
[1,2] in d
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    [1,2] in d
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
12.2 in d
False
12 in d
True

d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}




d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: {2, 3}, 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[8]='dict'
d
{1: 1, 2: 1.2, 3: (1+2j), 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[3]=23
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[5]
[1, 2]
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: [1, 2], 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[5]=3
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2}
d[13]=100
d[14]=101
d[15]=108
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2, 13: 100, 14: 101, 15: 108}


d.update({16:500,17:700})
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}


d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}
d.pop(2)
1.2
d.pop(12)
2
d
{1: 1, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}
d.del(5)
SyntaxError: invalid syntax
del(5)
SyntaxError: cannot delete literal

del d[5]
d
{1: 1, 3: 23, 4: 'str', 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}

del d[9]
d
{1: 1, 3: 23, 4: 'str', 6: (5, 6), 7: [{8, 9}], 8: 'dict', 10: False, 11: 1, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}

d.clear()
d
{}


d={1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}
d
{1: 1, 2: 1.2, 3: 23, 4: 'str', 5: 3, 6: (5, 6), 7: [{8, 9}], 8: 'dict', 9: {1: 1, 5: 5}, 10: False, 11: 1, 12: 2, 13: 100, 14: 101, 15: 108, 16: 500, 17: 700}
d.keys()
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
d.values()
dict_values([1, 1.2, 23, 'str', 3, (5, 6), [{8, 9}], 'dict', {1: 1, 5: 5}, False, 1, 2, 100, 101, 108, 500, 700])
d.items()
dict_items([(1, 1), (2, 1.2), (3, 23), (4, 'str'), (5, 3), (6, (5, 6)), (7, [{8, 9}]), (8, 'dict'), (9, {1: 1, 5: 5}), (10, False), (11, 1), (12, 2), (13, 100), (14, 101), (15, 108), (16, 500), (17, 700)])
len(d)
17
sorted(d)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
max(d)
17
mi(d)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    mi(d)
NameError: name 'mi' is not defined. Did you mean: 'min'?
min(d)
1

a={1:1,2:2}
b=a
b[3]=3
a
{1: 1, 2: 2, 3: 3}
b
{1: 1, 2: 2, 3: 3}
c=a.copy()
a
{1: 1, 2: 2, 3: 3}
c
{1: 1, 2: 2, 3: 3}
c[4]=4
c
{1: 1, 2: 2, 3: 3, 4: 4}
a
{1: 1, 2: 2, 3: 3}

>>> 
>>> 
>>> 
>>> d.dict.fromkeys(['a','b','c','d','e'],0)
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    d.dict.fromkeys(['a','b','c','d','e'],0)
AttributeError: 'dict' object has no attribute 'dict'
>>> 
>>> 
>>> 
>>> 
>>> d=dict.fromkeys(["a","b","c","d","e"],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> d=dict.fromkeys(['a','b','c','d','e'],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> d.setdefault('a')
0
>>> d.setdefault('h')
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
>>> d.setdefault('k',1)
1
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> d.setdefault('c',1)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> 
>>> 
>>> 
>>> 
>>> s=frozenset({1,2,3,4,5})
>>> s
frozenset({1, 2, 3, 4, 5})
>>> len(s)
5
>>> max(s)
5
>>> min(s)
1
>>> type(s)
<class 'frozenset'>
