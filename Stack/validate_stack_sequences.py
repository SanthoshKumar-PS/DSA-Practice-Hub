def validateStackSequences(pushed, popped):
    stack = []
    left = 0
    for num in pushed:
        stack.append(num)
        while stack and popped[left] == stack[-1]:
            stack.pop()
            del popped[0]
        print(stack)
    return left == len(popped) - 1


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

print(validateStackSequences(pushed,popped))