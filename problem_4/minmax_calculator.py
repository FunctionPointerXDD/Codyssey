
def main():
    raw = input("numbers: ")
    tokens = raw.split()
    nums = []

    for tok in tokens:
        try:
            nums.append(float(tok))
        except ValueError:
            print("Invalid input.")
            return

    if not nums:
        print("Invalid input.")
        return

    max_val = nums[0]
    min_val = nums[0]

    for n in nums[1:]:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n

    print(f"Min: {min_val}, Max: {max_val}")

if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
