# Interleave the First Half of the Queue with the Second Half
# 🔹 Input: 1 2 3 4 5 6
# 🔹 Output: 1 4 2 5 3 6

def interleave(inp):
    result=[]
    array=list(inp)
    n=len(array)
    if n%2!=0:
        result.append(inp[n//2])
        array=array[:n//2]+array[n//2+1:]

    mid=n//2
    first_half=array[:mid]
    second_half=array[mid:]
    for i in range(len(first_half)):
        result.append(first_half[i])
        result.append(second_half[i])

    return result




inp=[1,2,3,4,5]
print(interleave(inp))
inp=[1,2,3,4,5,6]
print(interleave(inp))