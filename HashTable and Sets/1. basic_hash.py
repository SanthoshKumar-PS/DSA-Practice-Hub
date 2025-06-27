my_dic = {}

my_dic["apple"] = 3
my_dic["banana"] = 5

print(my_dic["apple"])

if "banana" in my_dic:
    print("Exists")

del my_dic["banana"]

for key, value in my_dic.items():
    print(key, value)

print(my_dic.get("cherry", 0))
# 3
# Exists
# apple 3
# 0
