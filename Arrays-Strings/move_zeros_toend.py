#Move all zeros to the end of the array
def zeros_end(arr):
    count_zero=arr.count(0)
    for i in range(count_zero):
        arr.remove(0)
        arr.append(0)
    return arr

arr = [0, 1, 0, 3, 12]
print(zeros_end(arr))
