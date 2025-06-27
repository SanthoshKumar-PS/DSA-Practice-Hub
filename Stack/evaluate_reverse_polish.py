def evalRPN( tokens):
    stack = []
    for char in tokens:
        print(stack)
        if char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            last=stack.pop()
            first=stack.pop()
            stack.append(first -last)
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        elif char == '/':
            last=stack.pop()
            first=stack.pop()
            stack.append(int(first/last))
        else:
            stack.append(int(char))
    return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


print(evalRPN(tokens))