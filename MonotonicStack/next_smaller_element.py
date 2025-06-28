
nums=[2,1,5,6,2,3]
n=len(nums)
result=[-1]*n
stack=[]

for i,num in enumerate(nums):
    while stack and nums[stack[-1]]>num:
        result[stack.pop()]=num
    stack.append(i)
print(result)