#Sort an array of 0s, 1s, and 2s(Dutch National Flag Problem)

def dutch_national(arr):
    low = 0  # pointer for next 0
    mid = 0  # current element
    high = len(arr) - 1  # pointer for next 2

    while mid <= high:
        if arr[mid] == 0:
            print(arr)
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


arr = [2, 1, 0, 2, 0, 1]
print(dutch_national(arr))
