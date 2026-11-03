data=('admin@gmail.com','admin@123')

gmail=input("enter the mail: ")
password=input("enter the pasword: ")

if (gmail,password)==data:
    print("loginsucesseful")
else:
    print("invalid login") 
    





seats={
    's1':'booked',
    's2':'available',
    's3':'available',
    's4':'available',
    's5':'booked',
    's6':'available',
    's7':'available'
}

seatno=input("enter the seatno(sn): ")
if seatno in seats and seats[seatno]=='available':
    seats[seatno]='booked'
    print(f'{seatno} is successfuly booked')
    print(seats)
else:
    print(f'{seatno} is not available')






products={
    'laptop':{'price':40000,'stock':20},
    'mouse':{'price':500,'stock':0},
    'keyboard':{'price':2500,'stock':25},
    'tab':{'price':25000,'stock':5},
    'phone':{'price':80000,'stock':18},   
}

search=input('enter the product name: ')
if search in products and products[search]['stock']>0:
    print(f'you can buy{search}at this price:${products[search]['price']}')
else:
    print(f'{search } is not available')

