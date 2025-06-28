# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

temperatures= [73,74,75,71,69,72,76,73]
n=len(temperatures)
result=[0]*n
stack=[]
for i,num in enumerate(temperatures):
    while stack and temperatures[stack[-1]]<num:
        result[stack[-1]]=i-stack[-1]
        stack.pop()
    stack.append(i)
print(result)