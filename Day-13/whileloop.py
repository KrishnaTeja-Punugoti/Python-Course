#initial
#while condition
    #stmt
    #update

'''
#removing an element from list

l=[1,2,0,2,3,3,0,0,0,4,5,0,5,0,5,0,2,0,0,0,7]
while 0 in l:
    l.remove(0)

print(l)

'''



'''

i=1
while i<11:
    print(i)
    i+=1

'''


'''
i=10
while i>0:
    print(i)
    i-=1

'''


'''

i=2
while i<201:
    print(i)
    i+=2

'''


'''

i=5
while i<101:
    print(i)
    i+=5

'''



'''
# using break 


a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(a):
    if a[i]==5:
        break
    print(i,a[i])
    i+=1
'''


'''
# using continue

a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(a)-1:
    i+=1
    if a[i]==5:
        continue
    print(i,a[i])
    
'''



c='pythonprogramming'
i=0
j=len(c)-1

while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i],c[j])

    i+=1
    j-=1
