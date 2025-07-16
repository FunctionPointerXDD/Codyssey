##test 1234

def is_valid(tok: str) -> bool:
    bad_input = {"nan", "-nan", "+nan", "inf", "+inf", "-inf"}
    if tok.lower() in bad_input:
        return False
    return True

def bubble_sort(arr: list[float]) -> list[float]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp =  arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
    return arr

def main():
    try:
        raw = input("numbers: ")
        tokens = raw.split()
        nums = []

        for tok in tokens:
            if is_valid(tok):
                nums.append(float(tok))
            else:
                raise ValueError
        if not nums:
            raise ValueError
        
        sorted_nums = bubble_sort(nums)
        print("Sorted:", end=' ')
        for n in sorted_nums:
            print(n, end=' ')
        print('')

    except ValueError:
        print("Invalid input.")
        return

if __name__ =="__main__":
    main()