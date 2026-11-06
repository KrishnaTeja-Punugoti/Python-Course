'''

pin=12345
for i in range(5):
    epin=int(input('enter the pin: '))
    if epin==pin:
        print('login successful')
        break
    else:
        print('invalid pin')
else:
    print("max attempts reached! try again after 30 seconds")

'''




'''

l=[2,4,6,7,2,450,90,25,34,56,40]
search=int(input('enter the number: '))
for i in range(len(l)):
    if l[i]==search:
        print(f'{search}, is found at {i}')
        break
    else:
        print(f'{search}, is not found')

'''




c={1,2,43,56,8,48,67,5}
for i in enumerate(c):     #string         
    print(i[0],i[1])

c=[1,2,43,56,8,48,67,5]
for i in enumerate(c):     #list
    print(i[0],i[1])

c=(1,2,43,56,8,48,67,5)
for i in enumerate(c):     #tuple
    print(i[0],i[1])

c={'k1':'v1','k2':'v2','k3':'v3'}
for i in enumerate(c):
    print(i[0],i[1])