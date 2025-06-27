# Given two sentences, check if they have the same words with the same frequencies (case-insensitive).
#
# Input: "The cat sat" vs "Sat the cat" → True
from collections import defaultdict


def two_senteced_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    dic1=defaultdict(int)
    dic2=defaultdict(int)
    for i in range(len(str1)):
        dic1[str1[i].lower()]+=1
        dic2[str2[i].lower()]+=1
    if dic1==dic2:
        return True
    return False



str1="The cat sat"
str2="Sat the cat"
print(two_senteced_anagram(str1,str2))