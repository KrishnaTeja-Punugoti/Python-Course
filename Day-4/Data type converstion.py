Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
b=10.3
b
10.3
int(b)
10
complex(b)
(10.3+0j)
str(b)
'10.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
c=5+9j
c
(5+9j)
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str
<class 'str'>
(
str(c)
'(5+9j)'
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
str='1,2,3,4,5'
s='1,2,3,4,5'
s
'1,2,3,4,5'
int(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
float(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: '1,2,3,4,5'
bool(s)
True
list(s)
['1', ',', '2', ',', '3', ',', '4', ',', '5']
dict(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> set(s)
{'5', '2', '1', ',', '4', '3'}
>>> tuple(s)
('1', ',', '2', ',', '3', ',', '4', ',', '5')
>>> t=(1,3,2,5,4)
>>> t
(1, 3, 2, 5, 4)
>>> tuple(t)
(1, 3, 2, 5, 4)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    str(t)
TypeError: 'str' object is not callable
>>> bool(t)
True
>>> list(t)
[1, 3, 2, 5, 4]
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> set(t)
{1, 2, 3, 4, 5}
>>> tuple(t)
(1, 3, 2, 5, 4)
