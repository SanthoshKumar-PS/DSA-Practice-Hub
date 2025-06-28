# Input: [1, 2, 1]
# Output: [2, -1, 2]
#
# Input: [5, 4, 3, 2, 1]
# Output: [-1, 5, 5, 5, 5]

nums=[1,2,1]
n=len(nums)
result=[-1]*n
stack=[]
for i in range(len(nums)*2):
    curr_index=i%n
    while stack and nums[stack[-1]]<nums[curr_index]:
        result[stack[-1]]=nums[curr_index]
        stack.pop()
    if i<n:
        stack.append(curr_index)

print(result)
