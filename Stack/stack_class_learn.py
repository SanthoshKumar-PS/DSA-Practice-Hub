from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,num):
        self.container.append(num)
    def peek(self):
        return self.container[-1]
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    def isEmpty(self):
        return  len(self.container)==0

stack=Stack()
stack.push(5)
stack.push(10)
print(stack.size())
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())