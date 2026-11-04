''' 

s='codegnan'
for i in s:
    print(i)

a=input("enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)
        
'''



'''

s=[1,2,3,4,5]
for i in s:
    print(i)



a=list(map(int,input("enter the numbers: ").split()))
for i in a:
    if i%2==0:
        print(i)

'''




'''
s=(1,2,3,4,5)
for i in s:
    print(i)


sumoftuple=0
a=tuple(map(int,input("enter the numbers: ").split()))
for i in a:
    sumoftuple+=i
    print("sum of tuple:",sumoftuple)

'''


''' 

s={438,546,34,42,24,55,77}
for i in s:
    print(i)


max=0
a=set(map(int,input("enter the numbers: ").split()))
for i in a:
    if i>max:
        max=i
    print("max of set:",max)

'''




'''

marks={'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    print(i,marks[i])


sum=0
marks={'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    sum+=marks[i]
    print("total marks:",sum)

'''




'''

for i in range(1,11):
    print(i,end=' ')

for i in range(20,0,-1):
    print(i,end=' ')

for i in range(2,101,2):
    print(i,end=' ')

'''



'''

n=int(input('enter the table number: '))

for i in range(1,11):
    print(f'{n}*{i}={n*i}')

'''



'''

c='codegnan'
for i in range(len(c)):
    print(c[i],i,end=' ')

'''




'''

c=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(len(c)):
    if c[i]%2==0:
        sum+=i
        print(sum)

'''



#brake and continue methods 
'''

for i in range(1,21):
    if i ==5:
        break
    print(i)

for i in range(1,21):
    if i==5:
        continue
    print(i)

'''




#pass method


for i in range(1,11):
    pass

if True:
    pass

class booking:
    pass

def func():
    pass