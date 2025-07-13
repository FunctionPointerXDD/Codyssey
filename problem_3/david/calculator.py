
def add(a, b) -> int:
    return a + b

def subtract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b

def divide(a, b) -> float:
    if b == 0:
        print("Error:Division by zero.")
        return None
    return a / b

if __name__ == "__main__":
    try:
        a = int(input("input number1: "))
        b = int(input("input number2: "))
    except:
        print("Invalid input number.")
    
    op = input("input operator: ")
    if op == '+':
        print("Result: ", add(a, b))
    elif op == '-':
        print("Result: ", subtract(a, b))
    elif op == '*':
        print("Result: ", multiply(a, b))
    elif op == '/':
        result = divide(a, b)
        if result is not None:
            print("Result: ", divide(a, b))
    else:
        print("Invalid operator.")




        
