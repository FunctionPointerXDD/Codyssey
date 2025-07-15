
def main():
    raw = input("numbers: ")
    tokens = raw.split()

    nums = []
    for tok in tokens:
        try:
            nums.append(float(tok))
        except ValueError:
            raise ValueError("Invaid input.")

    max_val : int = -2147483648
    min_val : int = 2147483647
    for n in nums:
        if n > max_val:
            max_val = n
    for n in nums:
        if n < min_val:
            min_val = n

    print(f"Min: {min_val}, Max: {max_val}")

if __name__ =="__main__":
    main()
