# Simple Python Calculator for Basic Operations

def calculate():
    print("=== Welcome to My Python Calculator ===")
    
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Pick an operation: +  -  *  /")
        op = input("Your choice: ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("You can’t divide by zero!")
        else:
            print("That operation is not supported.")
    except ValueError:
        print("Please enter valid numbers!")
        
# Run it
calculate()

