from collections import defaultdict

counter=defaultdict(list)

fruits=['apple','orange','mango','lemon','avacado','plum','papaya','pineapple']

for fruit in fruits:
    counter[fruit[0]].append(fruit)

print(counter)