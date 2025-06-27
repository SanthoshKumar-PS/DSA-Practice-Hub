
def happy_number(n):
    seen=set()
    while n not in seen:
        print(n)
        seen.add(n)
        n= sum([int(x)**2 for x in str(n)])
    print(seen)
    return n==1


19


print(happy_number(19))