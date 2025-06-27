# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

def next_greater_circular(nums):
    result=[-1]*len(nums)
    stack=[]
    for i in range(len(nums)):
        while stack and nums[i]>nums[stack[-1]]:
            index=stack.pop()
            result[index]=nums[i]

        stack.append(i)
    for i in range(len(nums)):
        while stack and nums[i]>nums[stack[-1]]:
            index=stack.pop()
            result[index]=nums[i]

        stack.append(i)

    return result



nums = [1, 2, 3, 4, 3]
print(next_greater_circular(nums))