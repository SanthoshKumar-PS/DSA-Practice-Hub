# Check for Palindrome using Queue
# Check whether a given string is a palindrome using a queue and a stack.
#
# 🔹 Input: "madam"
# 🔹 Output: True

def check_palindrome(queue):
    while len(queue) > 1:
        if queue.popleft() == queue.pop():
            continue
        else:
            return False
    return True

from collections import deque
inp="madam"
queue=deque(inp)
print(check_palindrome(queue))



