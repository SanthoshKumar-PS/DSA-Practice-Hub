from itertools import product

input=["abc","def","geh"]
result=[(p) for p in product(*input)]
print(result)

result=[''.join(p) for p in product(*input)]
print(result)