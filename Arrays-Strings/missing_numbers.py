#Find the missing number in a given range(1 to n)

def missing_numbers(arr, n):
    total = sum(arr)
    req = (n * (n + 1)) / 2
    return int(req - total)


arr = [1, 2, 3, 5, 6]
n = 6
print(missing_numbers(arr, n))
