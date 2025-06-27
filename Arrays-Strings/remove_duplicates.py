#Remove duplicates from an array
arr=[1,2,3,4,5,4,3,2,1]
new_arr=[]
for num in arr:
    if num not in new_arr:
        new_arr.append(num)
print(new_arr)

##another solution
arr=[1,2,3,4,5,4,3,2,1]

new_arr=list(set(arr))
print(new_arr)
