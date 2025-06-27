from collections import defaultdict


def groupAnagrams( strs):
    my_dic = defaultdict(list)
    for str1 in strs:
        sorted_str = tuple(sorted(str1))
        my_dic[sorted_str].append(str1)
    print(my_dic)
    return []

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))