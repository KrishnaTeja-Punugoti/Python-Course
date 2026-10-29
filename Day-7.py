Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programmming'
s
'python programmming'
s.startswith('P')
False
s.startswith('p')
True
s.endswith('g')
True
s.endswith('o')
False
s.endswith('ing')
True
s.endswith('ting')
False
s.startswith('pyt')
True
s.startswith('pyto')
False


's'.islower()
True
's'.isupper()
False
'U'.islower()
False
'U'.isupper()
True


'codegan@'.isalpha()
False
'codegan12'.isalpha()
False
'codegan'.isalpha()
True
'codegan12'.isalnum()
True
'codegan@12'.isalnum()
False
'codegan@'.isalnum()
False
'codegan'.isalnum()
True
'12'.isalnum()
True


s
'python programmming'
s.istitle()
False
S.istitle()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    S.istitle()
NameError: name 'S' is not defined. Did you mean: 's'?
s.istitle()
False


s
'python programmming'
s.istitle()
False


'myvar'isidentifier()
SyntaxError: invalid syntax
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False


' '.isspace
<built-in method isspace of str object at 0x00007FFF41C94CC8>
' '.isspace()
True
' 1'.isspace()
False

'123'.isdecimal
<built-in method isdecimal of str object at 0x0000024E723522B0>
'123'.isdecimal()
True
'123'.isdigit()
True
'123'.isnumeric()
True


'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']

'a,b,c,d'.split(',',2)
['a', 'b', 'c,d']
'a,b,c,d'.split('-',2)
['a,b,c,d']
'a,b,c,d'.rsplit('-',2)
['a,b,c,d']


'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
'a-b-c-d'.lsplit('-',2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    'a-b-c-d'.lsplit('-',2)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
'a-b-c-d'.lsplit('-')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    'a-b-c-d'.lsplit('-')
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
'a-b-c-d'.rsplit()
['a-b-c-d']
'a-b-c-d'.lsplit()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    'a-b-c-d'.lsplit()
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?



s='
SyntaxError: unterminated string literal (detected at line 1)
s='''
hellow
world
python'''
s
'\nhellow\nworld\npython'
s.splitlines()
['', 'hellow', 'world', 'python']
l=['a',,'b','c','d']
SyntaxError: invalid syntax
l=['a','b','c','d']
l
['a', 'b', 'c', 'd']
'-'.join.(l)
SyntaxError: invalid syntax
'-'.join.(l)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

'@'.join(l)
'a@b@c@d'
'-'.join(l)
'a-b-c-d'
'_'.join(l)
'a_b_c_d'
' '.join(l)
'a b c d'
''.join(l)
'abcd'


s='a-b-c-d'
s
'a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
s.partition('-')
('a', '-', 'b-c-d')
'python.py'.partition(".")
('python', '.', 'py')
s='hellow '
s
'hellow '
s.encode()]
SyntaxError: unmatched ']'
s.encode()
b'hellow '
"hellow 😀😀".encode()
b'hellow \xf0\x9f\x98\x80\xf0\x9f\x98\x80'
"Krishna 😀 Teja 😀"encode()
SyntaxError: invalid syntax
"Krishna 😀 Teja 😀".encode()
b'Krishna \xf0\x9f\x98\x80 Teja \xf0\x9f\x98\x80'














l[]
SyntaxError: invalid syntax




l=[]
l=l.list()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    l=l.list()
AttributeError: 'list' object has no attribute 'list'
l=list()
l=[1,2,3,4,5]
l=list([1,2,3,4,5])
l
[1, 2, 3, 4, 5]


#mut ord dup het dyn
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l=[1,2,3,4,5,5]
l
[1, 2, 3, 4, 5, 5]
l=[1,1.2,3+5j,'str',[1,2],(1,2),{1,2},{1:2},false,none]
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    l=[1,1.2,3+5j,'str',[1,2],(1,2),{1,2},{1:2},false,none]
NameError: name 'false' is not defined. Did you mean: 'False'?
l=[1,1.2,3+5j,'str',[1,2],(1,2),{1,2},{1:2},false,none]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    l=[1,1.2,3+5j,'str',[1,2],(1,2),{1,2},{1:2},false,none]
NameError: name 'false' is not defined. Did you mean: 'False'?


l=[1,1.2,3+5j,'str',[1,2],(1,2),{1,2},{1:2}, False,None]
l
[1, 1.2, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]


l=['python','java','c','c++','flask','fastapi','mysql','aws']
l
['python', 'java', 'c', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
l[0]
'python'
l[-1]
'aws'
l[2]
'c'
l[:3]
['python', 'java', 'c']
l-3:]
SyntaxError: unmatched ']'
l[-3:]
['fastapi', 'mysql', 'aws']
l[2:5]
['c', 'c++', 'flask']
l[2::4]
['c', 'mysql']
l=[1::2]
SyntaxError: invalid syntax
l[1::2]
['java', 'c++', 'fastapi', 'aws']
l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c++', 'c', 'java', 'python']
l[-3:-6:-1]
['fastapi', 'flask', 'c++']
['java', 'c++', 'fastapi', 'aws']
['java', 'c++', 'fastapi', 'aws']

"c++" in l
True
"c+" not in l
True
"c++" not in l
False
"java" in l
True


code
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    code
NameError: name 'code' is not defined. Did you forget to import 'code'?
len(l)
8
sorted(l)
['aws', 'c', 'c++', 'fastapi', 'flask', 'java', 'mysql', 'python']
>>> max(l)
'python'
>>> min(l)
'aws'
>>> 
>>> id(l)
2535943880384
>>> l[1]
'java'
>>> l[1]='html'
>>> l
['python', 'html', 'c', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
>>> id(1)
140734297035896
>>> l[2]
'c'
>>> l[2]='css'
>>> l
['python', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
>>> 
>>> l.insert[1,'c']
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    l.insert[1,'c']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> l.append('a')
>>> l
['python', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 'a']
>>> l.append('b')
>>> l
['python', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 'a', 'b']
>>> 
>>> l.append('c')
>>> l
['python', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c']
>>> 
>>> l.extend([1,2,3,4,5])
>>> l
['python', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 5]
>>> l.insert(1,'java')
>>> l
['python', 'java', 'html', 'css', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 'a', 'b', 'c', 1, 2, 3, 4, 5]
