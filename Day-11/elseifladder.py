print('welcome to the weekend palnner')
budget=int(input('enter the budget: '))

print('you can go for',end=' ')
if budget>10000:
    print('trip')
elif budget>10000:
    print('resort')
elif budget>5000:
    print('cafe')
elif budget>2000:
    print('movie')
elif budget>1000:
    print('street shooping')

else:
    print('sleep')