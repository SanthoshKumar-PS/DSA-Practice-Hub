#Find all pairs in an array whose sum is equal to a given number

def subarr_sum(arr,n):
    ans=set()
    for i in range(0,len(arr)):
        required_number=n-arr[i]
        if required_number in arr:
            ans.add(tuple(sorted((arr[i],required_number))))
    return list(ans)
arr=[1,2,3,4,5,6]
n=6
print(subarr_sum(arr,n))
