def titleToNumber(columnTitle):
    n = len(columnTitle)
    ans = 0
    index = 1

    for i in range(n - 1, -1, -1):
        char_value = ord(columnTitle[i]) - ord('A')
        char_value=(char_value+1)
        ans += (char_value * index)
        index *= 26

    return ans

print(titleToNumber("ZY"))