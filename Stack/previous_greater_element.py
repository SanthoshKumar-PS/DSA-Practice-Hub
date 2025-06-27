# input nums = [2, 1, 5, 3, 6]
#output [-1,2,-1,5,-1]

def prev_greater_elements(nums):
    result=[-1]*len(nums)
    stack=[]
    for i in range(len(nums)-1,-1,-1):
        while stack and nums[i]>nums[stack[-1]]:
            index=stack.pop()
            result[index]=nums[i]

        stack.append(i)
    return result



nums = [2, 1, 5, 3, 6]
print(prev_greater_elements(nums))