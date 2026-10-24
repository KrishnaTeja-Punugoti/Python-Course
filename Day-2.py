Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import Keyword
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import Keyword
ModuleNotFoundError: No module named 'Keyword'
import keyword
print(len(keyword.kwlist))
... 
35
>>> print(keyword.kwlist)
... 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import Keyword
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import Keyword
ModuleNotFoundError: No module named 'Keyword'
>>> import keyword
>>> print(keyword.kwlist)
... 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
... 
35
>>> 
>>> a=10
>>> b=20
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
20
>>> c
30
