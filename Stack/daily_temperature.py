# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def daily_temperatures(temperatures):
    result=[0]*len(temperatures)
    stack=[]
    for i in range(len(temperatures)):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            index=stack.pop()
            result[index]=i-index

        stack.append(i)
    return result



temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temperatures))