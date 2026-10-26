Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
9//2
4
a%b
10
a=10
b=20
a5b
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a5b
NameError: name 'a5b' is not defined
a=20
b=10
a%b
0
a**a
104857600000000000000000000
2**2
4
2***2
SyntaxError: invalid syntax
3**3
27
 a
 
SyntaxError: unexpected indent

a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True


c=20
c
20
c=+10
c
10
c=c+10
c
20
c=C*5
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c=C*5
NameError: name 'C' is not defined. Did you mean: 'c'?
c=c*5
c
100
c+=10
c
110
c-=10
c*=10
c
1000
c/=10
c
100.0
c-=10
c
90.0

a=20
a
20
a%2==0 and a>10
True
a%2==0 and a>20
False
a%2==0 or a>10
True
a%2==0 or a>20
True
not a%2==0
False
not a>20
True



s="python"
'p' in s
True
'k' in s
False
't' not in s
False
's' not in s
True

l=["teja","krishna",'giri','chandu','dilli']
l
['teja', 'krishna', 'giri', 'chandu', 'dilli']
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
d={1:2,2:6,3:7,4:8,5:10}
d
{1: 2, 2: 6, 3: 7, 4: 8, 5: 10}
10 in d
False
5 in d
True
10 not in d
True
5 not in d
False



l=[1,2,3,4,5]
m=[1,2,3,4,5]
id9l)
SyntaxError: unmatched ')'
id(l)
2347912241088
>>> id(m)
2347912241280
>>> 
>>> l==m
True
>>> l is m
False
>>> n==m
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
>>> n=m
>>> n
[1, 2, 3, 4, 5]
>>> id (n)
2347912241280
>>> i is n
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    i is n
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> n is m
True
>>> n is not m
False
>>> n is l
False
>>> n is not l
True
>>> l is m
False
>>> l is n
False
>>> l is not m
True
>>> l is not n
True
