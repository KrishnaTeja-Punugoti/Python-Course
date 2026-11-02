bill=int(input("enter the bill:"))
status=eval(input("enter the raining:"))
if status:
    bill+=30
    print("extra delivery charges applied")
    print(f'final bill:{bill}')

product=input("enter the product:")
bestseller=eval(input("enter the status:"))
if bestseller:
    print(f'{product}is bestseller.')

batterycharge=int(input("enter the battery:"))
if batterycharge<20:
    print(f'battery is low:{batterycharge},charge your phone')

