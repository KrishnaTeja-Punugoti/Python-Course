Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s
NameError: name 's' is not defined
s='python'
s
'python'
t='programming'
t
'programming'
s+t
'pythonprogramming'
s*3
'pythonpythonpython'
t*3
'programmingprogrammingprogramming'
(s+t)*3
'pythonprogrammingpythonprogrammingpythonprogramming'
'*'*50
'**************************************************'
'*@#$%&'*50
'*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&*@#$%&'


s='python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s[5]
'n'
s[-5]
's'
s[-1]
'i'
s[0 to 5]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s[1 to 5]
SyntaxError: invalid syntax. Perhaps you forgot a comma?


s
'python java flask mysql fastapi'
s[0:6:1]
'python'
s[:6]
'python'
s[7:11:0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[7:11:0]
ValueError: slice step cannot be zero
s[7:11]
'java'
s[7:11:1]
'java'
s[24:]
'fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s=[:-1]
SyntaxError: invalid syntax
s=[-1:]
SyntaxError: invalid syntax
s=[-2:]
SyntaxError: invalid syntax
s=[-7:]
SyntaxError: invalid syntax
s=[:-1]
SyntaxError: invalid syntax
s[:-1]
'python java flask mysql fastap'
s[:-7]
'python java flask mysql '
s[-7:]
'fastapi'
s[-7:-1:0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[-7:-1:0]
ValueError: slice step cannot be zero
s[-1:-7:0]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s[-1:-7:0]
ValueError: slice step cannot be zero
s[-15:-20:-1]
'ksalf'
s[-2:-7:-1]
'patsa'
s[-5:: -20:]
SyntaxError: invalid syntax
s[-5:: -20]
's '

s
'python java flask mysql fastapi'
'java' in s
True
'mySQL' in s
False
'mysql' in s
True
'python' not in s
False
'html' not in s
True

le(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    le(s)
NameError: name 'le' is not defined. Did you mean: 'len'?
len(s)
31



s
'python java flask mysql fastapi'
len(s)
31
ord('d')
100
ord('a')
97
ord('k')
107
ord('+')
43
ord('%')
37
ord('*')
42
chr(20)
'\x14'
chr('a')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    chr('a')
TypeError: 'str' object cannot be interpreted as an integer
chr(210)
'Ò'
chr(21)
'\x15'
max(s)
'y'
min(s)
' '
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']


s.upper(S)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.upper(S)
NameError: name 'S' is not defined. Did you mean: 's'?
s.uper(S)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.uper(S)
AttributeError: 'str' object has no attribute 'uper'. Did you mean: 'upper'?
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitalize()
'Python java flask mysql fastapi'
"PYTHON JAVA FLASK MYSQL FASTAPI".casefold()
'python java flask mysql fastapi'
'PYTHON JAVA FLASK MYSQL FASTAPI'
"PYTHaN JoVk FLASa MYSQi FASTAPl".casefold()
SyntaxError: multiple statements found while compiling a single statement
"PYTHaN JoVk FLASa MYSQi FASTAPl".casefold()
'pythan jovk flasa mysqi fastapl'



s.center(40,'-')
'----python java flask mysql fastapi-----'
s.center(40,'')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.center(40,'')
TypeError: The fill character must be exactly one character long
s.center(40,' ')
'    python java flask mysql fastapi     '
s.ljust(40.'*')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(40,'*')
'python java flask mysql fastapi*********'
s.rjust(40,'*')
'*********python java flask mysql fastapi'
"123".zfill(7)
'0000123'
"123456".zfill(7)
'0123456'
"12345674".zfill(7)
'12345674'
"1".zfill(7)
'0000001'


s
'python java flask mysql fastapi'
s.count('a')
5
s.count('p')
2
s.count('t')
2


s='   codeg  nan   '
s
'   codeg  nan   '
>>> s.strip()
'codeg  nan'
>>> s.lstrip()
'codeg  nan   '
>>> s.rstrip()
'   codeg  nan'
>>> s.rstrip('*')
'   codeg  nan   '
>>> 
>>> 
>>> 
>>> 
>>> s.replace("a","*")
'   codeg  n*n   '
>>> 'python java flask mysql fastapi'
... s=
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> s='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s.replace("a","*")
... 
'python j*v* fl*sk mysql f*st*pi'
>>> s.maketrans("apkqs","12345")
... 
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate("apkqs","12345")
... 
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    s.translate("apkqs","12345")
TypeError: str.translate() takes exactly one argument (2 given)
>>> 
>>> 
>>> s.translate(s.maketrans("apkqs","12345"))
... 
'2ython j1v1 fl153 my54l f15t12i'
