# Write a function that returns the first non-repeating character in a string.
# Example: "aabbccdef" → 'd'
from collections import defaultdict

def first_unique_character(word):
    my_dict = defaultdict(int)
    for let in word:
        my_dict[let] += 1
    for key, value in my_dict.items():
        if my_dict[key] == 1:
            return key
    return -1

word = "aabbccdef"
print(first_unique_character(word))