# Generate Binary Numbers from 1 to N
# Use a queue to generate binary numbers from 1 to N.
#
# 🔹 Input: N = 5
# 🔹 Output: 1 10 11 100 101

from collections import deque
def get_binary(n):
    array=[]
    while n>0:
        remainder=n%2
        array.append(str(remainder))
        n=n//2
    return ''.join(reversed(array))

queue=deque()

for n in range(5,0,-1):
    queue.appendleft(get_binary(n))
print(list(queue))


