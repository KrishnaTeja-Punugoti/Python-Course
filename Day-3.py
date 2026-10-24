Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=12.3
>>> type(b)
<class 'float'>
>>> c=2+5j
>>> type(c)
<class 'complex'>
>>> s="Teja"
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4,5]
>>> type(l)
<class 'list'>
>>> k=[1,2.3,5,"999",{1,2,3,4,5]]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> k=[1,2.3,5,"999",[1,2,3,4,5]]
>>> k
[1, 2.3, 5, '999', [1, 2, 3, 4, 5]]
>>> type(k)
<class 'list'>
>>> s="krishna"
>>> id(s)
2805817875344
>>> s+="teja"
>>> s
'krishnateja'
>>> id(s)
2805817928496
>>> l.append=["12]
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> l.append=["12"]
...           
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l.append=["12"]
AttributeError: 'list' object attribute 'append' is read-only
l.append=("12")
          
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l.append=("12")
AttributeError: 'list' object attribute 'append' is read-only
s={34,1323,12345,1323,34,55,5,6,5,7,6,5,5,5,5,9}
          
s
          
{34, 5, 6, 7, 9, 1323, 55, 12345}
type(s)
          
<class 'set'>

d={1:'one',2.4,3:[1,2,3],5:(1,23)}
          
SyntaxError: ':' expected after dictionary key
d={1:"one",2.4,3:[1,2,3],5:(1,23)}
          
SyntaxError: ':' expected after dictionary key
d={1:'one',2:4,3:[1,2,3],5:(1,23)}
          
d
          
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
type(d)
          
<class 'dict'>
pro={"pro_name":"laptop",'price':50000,'discount':10}
          
status=True
          
type(status)
          
<class 'bool'>
s=false
          
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s=false
NameError: name 'false' is not defined. Did you mean: 'False'?
s=False
          
s
          
False
type(s)
          
<class 'bool'>
s=None
          
type(s)
          
<class 'NoneType'>
