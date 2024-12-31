
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b
def floordiv(a,b):
    return a//b
operator={
            "+":add,
            "-":sub,
            "*":mul,
            "/":div,
            "%":mod,    
            "**":exp,
            "//":floordiv
        }

def calculator():
    n1 = int(input("Enter first number: "))
    flag = True
    while flag:
        
        for key in operator:
            print(key)
        op = input("Enter operator: ")
        n2 = int(input("Enter second number: "))
        function=operator[op]
        output = function(n1,n2)
        print(f"{n1} {op} {n2} = {output}")
        should_continue = input(f"Enter y to continue with the result {output}  or n to start a new calculation or x to exit")
        if should_continue == "y":
            n1 = output
        elif should_continue == "n":
            calculator()
        else:
            flag= False
            print("Goodbye")
calculator()