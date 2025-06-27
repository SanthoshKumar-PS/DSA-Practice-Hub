#nums = [5, 4, 3, 2, 1]
# Output: [4, 3, 2, 1, -1]


def next_smaller_elements(nums):
    result=[-1]*len(nums)
    stack=[]
    for i in range(len(nums)):
        while stack and nums[i]<nums[stack[-1]]:
            index=stack.pop()
            result[index]=nums[i]

        stack.append(i)
    return result



nums = [5, 4, 3, 2, 1]
print(next_smaller_elements(nums))