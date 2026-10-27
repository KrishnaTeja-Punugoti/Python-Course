Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5&14
4
11712
11712
11&12
8
8|9
9
11^12
7
~11
-12
!55
SyntaxError: invalid syntax
~55
-56
2<<2
8
8>>3
1
12~11
SyntaxError: invalid syntax
~554
-555
15>>3
1


a=input("enter the input")
enter the inputa=
a=input("enter the input:")
enter the input:teja
a
'teja'
a=input("enter the input:")
enter the input:234
a
'234'
a=int(input("enter the integer:"))
enter the integer:teja
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a=int(input("enter the integer:"))
ValueError: invalid literal for int() with base 10: 'teja'
a=int(input("enter the integer:"))
enter the integer:18
b=int(input("enter the integer:"))
enter the integer:18
b
18


f=float(input("enter the input:"))
enter the input:123
f
123.0
f=float(input("enter the input:"))
enter the input:64429
f
64429.0
f=float(input("enter the input:"))
enter the input:18.9
f
18.9
b=int(input("enter the integer:"))18.9
SyntaxError: invalid syntax




b=int(input("enter the integer:"))
enter the integer:358.945
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b=int(input("enter the integer:"))
ValueError: invalid literal for int() with base 10: '358.945'
b=int(input("enter the integer:"))
enter the integer:54
b
54


a=list(input())
12  44 6 5 5 5 5  55 98 78 67 
a
['1', '2', ' ', ' ', '4', '4', ' ', '6', ' ', '5', ' ', '5', ' ', '5', ' ', '5', ' ', ' ', '5', '5', ' ', '9', '8', ' ', '7', '8', ' ', '6', '7', ' ']
a=list(input().split())
a

a=list(input().split())
121 423 543 89 6879 
a
['121', '423', '543', '89', '6879']
list (map (int,a))
[121, 423, 543, 89, 6879]
a=list
list (map (int,input().split()))
12 76 986 57 7 96 5 75  
[12, 76, 986, 57, 7, 96, 5, 75]


list of str-  input().split()
SyntaxError: invalid syntax





input().split()
12 23 3223 42
['12', '23', '3223', '42']
a
<class 'list'>
a=input().split()
12 12 31 3 13 1  133 1 313 
a
['12', '12', '31', '3', '13', '1', '133', '1', '313']
a=list(map(float,input().split()))
23 13 13 1213 3 13 3 13
a
[23.0, 13.0, 13.0, 1213.0, 3.0, 13.0, 3.0, 13.0]
a=list(map(int,input().split()))
3 431 3 21 3 31 313 
a
[3, 431, 3, 21, 3, 31, 313]


a=tuple(input().split())
53 4232 1 31 13 1
a
('53', '4232', '1', '31', '13', '1')
a=tuple(map(float,input().split()))
 53442 2 68 4 6 18 41 351 6
a
(53442.0, 2.0, 68.0, 4.0, 6.0, 18.0, 41.0, 351.0, 6.0)
a=tuple(map(int,input().split()))

 651 165 4 41 2 15 41651 
a
(651, 165, 4, 41, 2, 15, 41651)


a=set(input().split())
646 44 641 641 6
a
{'646', '6', '641', '44'}
a=set(map(float,input().split()))
 654165 1 41 54 1 5165
a
{1.0, 41.0, 5165.0, 654165.0, 54.0}
a=set(map(int,input().split()))
651 5 1 61 61 61
a
{61, 1, 651, 5}


a,b,c=list(map(int,input().split()))
18 9 55
a
18
b
9
c
55
email.password=input().split()
teja@gmail.com 12345
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    email.password=input().split()
NameError: name 'email' is not defined. Did you mean: 'eval'? Or did you forget to import 'email'?
email,password=input().split()
teja@gmail.com 12345
email
'teja@gmail.com'
password
'12345'

a=eval(input())
[1,2,3]
a
[1, 2, 3]
a=eval(input())
"Krishna Teja"
a
'Krishna Teja'
a=eval(input())
(1,2,3)
a
(1, 2, 3)
a=eval(input())
{1,2,3}
a
{1, 2, 3}

>>> 
>>> 
>>> 
>>> c="Teja"
>>> a
{1, 2, 3}
>>> c="Teja"
>>> a=10
>>> b=10.2
>>> c
'Teja'
>>> a
10
>>> b
10.2
>>> c
'Teja'
>>> print(a,b,c)
10 10.2 Teja
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.2 c= Teja
>>> print("a=",a,"b=",b,"c=",c,sep=,,)
SyntaxError: expected argument value expression
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.2c=Teja
>>> print("a=",a,"b=",b,"c=",c,sep='-')
a=-10-b=-10.2-c=-Teja
>>> print("a=",a,"b=",b,"c=",c,end='\n\n')
a= 10 b= 10.2 c= Teja

>>> print("a=",a,"b=",b,"c=",c,end='@')
a= 10 b= 10.2 c= Teja@
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.2 c=Teja
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=Teja
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.20 c=Teja
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=Teja
>>> print('a={} b={} c={}'.format(b,c,a))
a=10.2 b=Teja c=10
