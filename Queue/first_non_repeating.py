#Problem: First Non-Repeating Character in a Stream
# Input stream: "a a b c"
# Output: "a - b c"
from tokenize import String

from collections import defaultdict,deque

inp="aabc"
inp=list(inp)
print(inp)
my_dic=defaultdict(int)
queue=deque()
for let in inp:
    my_dic[let]+=1
    if my_dic[let]==1:
        queue.append(let)
    else:
        queue.append('-')
print(''.join(queue))