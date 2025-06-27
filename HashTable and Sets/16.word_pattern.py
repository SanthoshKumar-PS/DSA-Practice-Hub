from collections import defaultdict


def wordPattern(pattern, s):
    dic = defaultdict()
    arr = s.split(' ')
    if len(arr) != len(pattern):
        return False
    for i, string in enumerate(arr):
        print(dic)
        if pattern[i] in dic and dic[pattern[i]] != string:
            return False
        dic[pattern[i]] = string
    return True

print(wordPattern("abba","dog cat cat dog"))