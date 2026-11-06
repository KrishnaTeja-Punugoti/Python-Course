#while loop peogram



'''

l=[12,9,3,4,5,10,5,2,4,5,2,4,5]

#example output first number+last number,secound first number +secound last number ,etc.,

i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1

''' 




'''

# progaram to print the total amount of bill using while loop

bill=0
while True:
    product=input('enter the product: ')
    if product=='stop':
        print('total bill:',bill)
        break
    price=int(input('enter the price: '))
    qua=int(input("enter the quantity: "))
    bill+=price*qua

'''




products={'apple':150,
      'banana':30,
      'kackfruit':100,
      'mango':80,
      'pineapple':90,
      'bluebarry':50,
      'dragonfruit':200
      }

print('welcome to the store'.center(50,'-'))   #to print the welcome banner
print('product name','price')         #to print the produts and prices

for i in products:
    print(i.ljust(12,' '),':',products[i])

carts={}
while True:
    cart=input('enter the product name(exit): ').lower()
    if cart=='exit':
        break
    qua=int(input('enter the quantity: '))
    carts[cart]=qua

print('bill'.center(50,'-'))
print('product name quantity ($)price')
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
    bill+=carts[i]*products[i]

print(f'total bill: ${bill}')
print('thanks for shopping')