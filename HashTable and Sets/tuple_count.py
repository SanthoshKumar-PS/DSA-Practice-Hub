from collections import defaultdict

tuple_set=[('A',2),('B',3),('C',5),('B',8),('A',7),('C',6)]
group_data=defaultdict(list)
counter=defaultdict(int)
for first in tuple_set:
    counter[first[0]]+=first[1]
    group_data[first[0]].append(first[1])

print(counter)
print(group_data)