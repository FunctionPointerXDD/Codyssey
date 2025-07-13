
if __name__ == "__main__":
    try:
        num = float(input())
    except:
        print("Invalid number input.")
        exit(1)
    try:
        expo = int(input())
    except:
        print("Invalid exponent input.")
        exit(1)
    
    Result = 1
    while expo > 0:
        Result *= num
        expo -= 1
    print(Result)
    

