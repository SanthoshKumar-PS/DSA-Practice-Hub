# Number to Binary
# Input 10
# Output 1010

n=10
array=[]
while n>0:
    remainder=n%2
    array.append(remainder)
    n=n//2
array.reverse()
print(''.join(str(x) for x in array))