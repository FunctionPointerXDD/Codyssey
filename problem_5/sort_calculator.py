
def is_valid(tok: str) -> bool:
    bad_input = {"nan", "-nan", "+nan", "inf", "+inf", "-inf"}
    if tok in bad_input:
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
    raw = input("numbers: ")
    tokens = raw.split()
    nums = []

    for tok in tokens:
        try:
            if is_valid(tok):
                nums.append(float(tok))
            else:
                raise ValueError
        except:
            raise ValueError("Invalid input.")
    
    sorted_nums = bubble_sort(nums)
    print("Sorted:", end=' ')
    for n in sorted_nums:
        print(n, end=' ')
    print('')

if __name__ =="__main__":
    main()