# Different functions for all operators
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def floorDiv(a, b):
    return a // b

def mod(a, b):
    return a % b
    
if __name__ == "__main__":
    print("~ ~ ~ WELCOME TO SIMPLE CALCULATOR ~ ~ ~")

    while True:
        print("---------------------------------")
        print(" 1. ADDITION       -> +")
        print(" 2. SUBTRACTION    -> -")
        print(" 3. MULTIPLICATION -> *")
        print(" 4. DIVISION       -> /")
        print(" 5. FLOOR DIVISION -> //")
        print(" 6. MODULUS        -> %")
        print(" 7. QUIT")
        operator = int(input("Enter an arithmetic operation to perform(1-7): "))
        if operator == 7:
            break
        
        # Takes two input 
        a = int(input("ENTER 1ST NO.: "))
        b = int(input("ENTER 2ND NO.: ")) 
        print("---------------------------------")
        
        if operator == 1: 
            print("the value of",a,"+",b,"is :", add(a, b))
        elif operator == 2:
            print("the value of",a,"-",b,"is :", sub(a, b))
        elif operator == 3:
            print("the value of",a,"*",b,"is :", float(mul(a, b)))
        elif operator == 4:
            print("the value of",a,"/",b,"is :", round(div(a, b),2))
        elif operator == 5:
            print("the value of",a,"//",b,"is :", float(floorDiv(a, b)))
        elif operator == 6:
            print("the value of",a,"%",b,"is :", float(mod(a, b)))
        else:
            print("Invalid input")   
    print("THANKS FOR USING THE CALCULATOR. HAVE A NICE DAY :)")
