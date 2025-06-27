# Find All Duplicates in a List
# Return all elements that appear more than once in a list.
# Example: [1, 3, 5, 3, 2, 1] → [3, 1]
from collections import defaultdict


def find_duplicates_in_list(nums):
    dic=defaultdict(int)
    arr=[]
    for n in nums:
        dic[n]+=1
        if dic[n]>1:
            arr.append(n)
    return arr


nums=[1,3,5,3,2,1]
print(find_duplicates_in_list(nums))