a = float(input("please enter first number: "))
b = float(input("please enter second number: "))
c = float(input("please enter third number: "))

if a>0 and b>0 and c>0:
    if( a+b>c and a+c>b and b+c>a):
        print("you can")
    else:
        print("you can not") 
else:
    print("Error")           