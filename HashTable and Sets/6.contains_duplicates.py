from collections import defaultdict
nums = [1,2,3,1]


def contains_duplicates(nums):
    my_dict=defaultdict(int)
    for num in nums:
        my_dict[num]+=1
        if(my_dict[num]>1):
            return True
    return False

print(contains_duplicates(nums))