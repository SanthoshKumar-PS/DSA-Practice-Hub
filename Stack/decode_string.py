def decodeString(s):
    stack=[]
    curNum=0
    curString=''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num * curString
        elif c.isdigit():
            curNum = curNum * 10 + int(c)
        else:
            curString += c
    return curString




s = "3[a]2[bc]"
print(decodeString(s))