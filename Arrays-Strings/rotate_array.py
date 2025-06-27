#Rotate the array by k positions.
arr=[5,6,3,4,12,3,65,34,12,9]
k=3
n=len(arr)
k=k%n
print(arr[k:]+arr[:k])

