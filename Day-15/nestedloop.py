'''

for row in range(3):
    for col in range(5):
        print(col,end=' ')      #end=' ' is used to print the values side by side
    print()                     #this default print is use to print the values if one col completed

'''


'''

#pattern programmes

for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

'''


'''

for i in range(5):
    for j in range(5):
        if (i+j)%2==0:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()


 #or below code


for i in range(5):       #i=row
    for j in range(5):   #j=col
        print(int((i+j)%2==0),end=' ')
    print()

'''



''' 

for i in range(5):
    for j in range(5):
        print(int((j%2==1)),end=' ')
    print()

#or 

for i in range(5):
    for j in range(5):
        print(j%2,end=' ')
    print()

'''



'''

c=1
for i in range(5):
    for j in range(5):
        print(c,end=' ')
        c+=1
    print()

'''



'''

for i in range(5):
    for j in range(5):
        print(int(i*j),end=' ')
    print()

#or

for i in range(5):
    for j in range(5):
        print(i*j,end=' ')
    print()

'''


'''

n=int(input('enter the size: '))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

'''



'''

n=5
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

'''