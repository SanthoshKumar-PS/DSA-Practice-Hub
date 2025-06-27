#Count the occurrences of a specific element

def CountOccu(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1

    return count


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
x = 2

print(CountOccu(arr, x))
