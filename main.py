num1=int(input("enter the number 1:-"))

num2=int(input("enter the number 2:-"))

arg=input("enter the value:-")

if arg=="+":
    print(int(num1+num2))
elif arg=="-":
    print(int(num1-num2))
elif arg=="*":
    print(int(num1*num2))
elif arg=="/":
    print(int(num1/num2))
else:
    print("error...  invalid argunment")

