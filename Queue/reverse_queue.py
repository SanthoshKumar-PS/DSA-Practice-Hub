from collections import deque

my_list=[1,2,3,4]
q=deque()

for n in my_list:
    q.appendleft(n
                 )
print(list(q))