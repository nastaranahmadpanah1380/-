import math
radical = math.sqrt
factorial = math.factorial
sin = math.sin
cos = math.cos
tan = math.tan
# type "1" = + - * / 
# type "2" = sin cos tan cot radical factorial

t = input( "please enter your type: ")
if t == "1":
    op = input( "please enter your operation: ")
    a = int(input( "please enter your number: "))

    if op == "sin":
        result = sin(math.radians(a))
        print(result)
    if op == "cos":
        result = cos(math.radians(a))
        print(result)    
    if op == "tan":
        result = tan(math.radians(a))
        print(result)
    if op == "cot":
        if sin(math.radians(a)) != 0:
            result = 1/(tan(math.radians(a))) 
        else:    
            result = "Error"
        print(result)      
    if op == "radical":
        if a >= 0:
            result = radical(a)
            print(result)    
    if op == "factorial":
        result = factorial(a)    
        print(result)

if t == "2":
    op = input( "please enter your operation: ")
    a = int(input( "please enter your first number: "))
    b = int(input( "please enter your second number: "))
    
    if op == "+": 
        result = a + b
        print(result)
    if op == "-": 
        result = a - b
        print(result)
    if op == "*": 
        result = a * b
        print(result)
    if op == "/":
        if b == 0:
            result = "ERROR"
        if b != 0:
            result = a / b  
            print(result)    
