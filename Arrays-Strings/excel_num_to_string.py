def convertToTitle(columnNumber):
    ans = ""
    while columnNumber >0:
        columnNumber-=1
        ans=chr(columnNumber%26 +ord('A'))+ans
        columnNumber//=26
    return ans

print(convertToTitle(701))

# ZY Z