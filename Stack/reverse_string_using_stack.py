

inp_str="We will win,not now. But one day, we will achieve";
stack=[]
for char in inp_str:
    stack.append(char)
result=''
while len(stack)!=0:
    result+=stack.pop()

print(result)