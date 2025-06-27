#Kadane’s Algorithm (Maximum Subarray Sum)
def kadanes_algo(arr):
    max_sum=arr[0]
    cur_sum=0
    for num in arr:
        if(cur_sum<0):
            cur_sum=0
        cur_sum+=num
        max_sum=max(max_sum,cur_sum)
    return max_sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadanes_algo(arr))
