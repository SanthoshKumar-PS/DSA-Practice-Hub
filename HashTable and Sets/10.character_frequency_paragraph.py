# Given a paragraph,
# return a dictionary of each character's frequency,ignoring punctuation and whitespace.
from collections import defaultdict


def character_frequency(paragraph):
    my_dic=defaultdict(int)
    for let in paragraph:
        if let.isalpha():
            my_dic[let.lower()]+=1
    return my_dic


paragraph="You can use a SnackBar in Flutter to show a short message at the bottom of the screen. It’s commonly used to give feedback, like showing “Password is incorrect.” The message appears for a few seconds and then disappears automatically."
print( character_frequency(paragraph));