my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(2)

print(1 in my_set)

my_set.remove(1)

for item in my_set:
    print(item)
# True
# 2