# input nums = [2, 1, 5, 3, 6]
# output [5, 5, 6, 6, -1]

def next_greater_elements(nums):
    result=[-1]*len(nums)
    stack=[]
    for i in range(len(nums)):
        while stack and nums[i]>nums[stack[-1]]:
            index=stack.pop()
            result[index]=nums[i]

        stack.append(i)
    return result


nums = [2, 1, 5, 3, 6]
print(next_greater_elements(nums))
