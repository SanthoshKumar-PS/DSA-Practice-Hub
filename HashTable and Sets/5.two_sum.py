from collections import defaultdict


nums=[2,7,11,15]
target=9
def two_sum(nums,target):
    my_dict=defaultdict(int)
    for i,num in enumerate(nums):
        if target-num in my_dict:
            return [my_dict[num],i]
        my_dict[num]=i

print(two_sum(nums,target))