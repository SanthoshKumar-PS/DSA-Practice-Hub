

nums=[2,1,5,6,2,3]
n=len(nums)
#expected 5,5,6,-1,3,-1
stack=[]
result=[-1]*n
for i,num in enumerate(nums):
    while stack and nums[stack[-1]]<num:
        result[stack[-1]]=num
        stack.pop()
    stack.append(i)
print(result)
