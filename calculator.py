def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def modulo(x,y):
    return x%y

print("select operation:")
print("1.addition")
print("2.substration")
print("3.multiplication")
print("4.division")
print("5.modulo")

choice=input("enter your choice:")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=='2':
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice=='3':
    print(num1,"*",num2,"=",mul(num1,num2))

elif choice=='4':
    print(num1,"/",num2,"=",div(num1,num2))

elif choice=='5':
    print(num1,"%",num2,"=",modulo(num1,num2))

else:
    print("invalid input")


