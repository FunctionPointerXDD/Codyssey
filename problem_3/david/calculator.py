
def add(a, b) -> int:
    return a + b

def subtract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b

def divide(a, b) -> float:
    return a / b

if __name__ == "__main__":
    try:
        a = float(input("input number1: "))
        b = float(input("input number2: "))
        a = int(a)
        b = int(b)
    
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
            raise ValueError('')

    except ValueError:
        
        print("Invalid input number.")
        exit(1)


        
