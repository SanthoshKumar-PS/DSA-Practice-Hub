#Find the duplicate element in an array with n+1 elements
def duplicate(arr):
    unique=set()
    for n in arr:
        if n not in unique:
            unique.add(n)
        else:
            return n
    return -1

arr = [1, 3, 4, 2,2]
print(duplicate(arr))
