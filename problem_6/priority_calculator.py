
def is_valid(tok: str) -> bool:
    bad_input = {"nan", "-nan", "+nan", "inf", "+inf", "-inf"}
    if tok.lower() in bad_input:
        return False
    return True

def add(a, b) -> int:
    return a + b

def subtract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b

def divide(a, b) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b

def tokenize(expr: str) -> list[str]:
    tokens = expr.split()
    ops = ['+', '-', '*', '/']
    n = len(tokens)

    if n < 3 or n % 2 == 0:
        raise ValueError("Invalid input.")

    for i, tk in enumerate(tokens):
        if i % 2 == 0:
            try:
                if is_valid(tk):
                    float(tk)
                else:
                    raise ValueError

            except ValueError:
                raise ValueError("Invalid input.")
        else:
            if tk not in ops:
                raise ValueError("Invalid input.")

    return tokens

def precedence(op: str) -> int: 
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def to_postfix(tokens: list[str]) -> list[str]:
    output: list[str] = []
    ops: list[str] = [] # like stack
    op_set = {'+', '-', '*', '/'}

    for tk in tokens:
        if tk in op_set:
            while ops and precedence(ops[-1]) >= precedence(tk):
                output.append(ops.pop())
            ops.append(tk)
        else:
            output.append(tk)

    while ops:
        output.append(ops.pop())
    return output
    
def eval_postfix(postfix: list[str]) -> float:
    stack: list[float] = []
    op_set = {'+', '-', '*', '/'}

    for tk in postfix:
        if tk in op_set:
            b = stack.pop()
            a = stack.pop()
            if tk == '+':
                res = add(a, b)
            elif tk == '-':
                res = subtract(a, b)
            elif tk == '*':
                res = multiply(a, b)
            elif tk == '/':
                res = divide(a, b)
            stack.append(res)
        else:
            stack.append(float(tk))

    return stack[0]

def main():
    while True:
        expr = input("calc: ")
        if expr == "exit":
            break

        try:
            tokens = tokenize(expr)
            postfix = to_postfix(tokens)
            res =  eval_postfix(postfix)
            print(res)
        except Exception as e:
            print("Error:", e)
        
if __name__ == "__main__":
    main()

