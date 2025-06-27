
def parantheses_balance_check(inp):
    stack=[]
    dic_match={
        '}':'{',
        ']':'[',
        ')':'('
    }

    for char in inp:
        if char=='{' or char =='[' or char=='(':
            stack.append(char)
        elif char=='}' or char ==']' or char==')':
            if len(stack)==0:
                return False
            if stack.pop()==dic_match[char]:
                continue
            else:
                return False
    return len(stack)==0



    return  stack


inp_str="{{}{a+b}}"
print(parantheses_balance_check(inp_str))
print(parantheses_balance_check("{{}}{}"))
print(parantheses_balance_check("{{{}})"))
print(parantheses_balance_check("(({}{}))"))
print(parantheses_balance_check("{{}}{}{}()()()"))