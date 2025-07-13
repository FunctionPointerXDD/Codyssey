
def main():
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
    if expo >= 0:
        while expo > 0:
            Result *= num
            expo -= 1
    else:
        if num == 0 and expo < 0:
            print("Error: Division by zero due to negative exponent to zero.")
        while expo < 0:
            Result /= num
            expo += 1
    print(Result)


if __name__ == "__main__":
    main()
