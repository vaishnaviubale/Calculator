
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b 
def divide(a,b):
    if y != 0:
        return a / b
    else:
        return "Cannot divide by zero. Please enter number greater than zero."
try:
    c = float(input("Enter first number: "))
    d = float(input("Enter second number: "))
    operation = input("Enter the operation to be done '(+ , - , * , /): '")

    if operation == '+':
        result = add(c,d)
    
    elif operation == '-':
        result = subtract(c,d)
    
    elif operation == '*':
        result = multiply(c,d)
    
    elif operation == '/':
        result = divide(c,d)
    
    else:
        result = "Invalid operation, please select a correct operation."
    
    print(f"The answer for the operation {operation} is {result}")

except ValueError:
    print("Invalid Number. Please enter a valid number.")

