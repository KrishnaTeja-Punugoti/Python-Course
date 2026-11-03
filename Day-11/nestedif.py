data={
    'krishna':{'status':True,'python':96,'mysql':95,'fastapi':97},
    'praveen':{'status':True,'python':86,'mysql':85,'fastapi':77},
    'eswar':{'status':True,'python':66,'mysql':65,'fastapi':77},
    'surya':{'status':True,'python':46,'mysql':35,'fastapi':37},
    'raghu':{'status':True,'python':26,'mysql':35,'fastapi':27},
    'teja':{'status':False,'python':None,'mysql':None,'fastai':None}
}

name=input("enter the name: ")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['fastapi']
        avg =total/3
        if avg>80:
            print(f'{name},congrates you got the first grade')
        elif avg>60:
            print(f'{name},good,work hard')
        elif avg>40:
            print(f'{name},work hard')
        elif avg>35:
            print(f'{name},just pass,work hard')
        else:
            print(f'{name},you fail,better luck next time')

    else:
        print(f"{name},didn't attend the exam,bring your parents")
else:
    print(f'{name},data not found')
