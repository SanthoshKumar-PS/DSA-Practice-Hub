#Find the second largest and second smallest element
arr=[2,1,2,3,4,5,5,4,3,2,1]
new_set=set()
new_arr=[]
for num in arr:
    if num not in new_set:
        new_arr.append(num)
        new_set.add(num)
print(new_arr[-2],new_arr[1])
