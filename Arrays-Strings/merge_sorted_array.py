#Merge sorted array

a1=[1,3,5,7]
a2=[2,4,6,8,9]
i=j=0
arr=[]
while i<len(a1) and j<len(a2):
    if a1[i]>a2[j]:
        arr.append(a2[j])
        j+=1
    else:
        arr.append(a1[i])
        i+=1
arr.extend(a1[i:])
arr.extend(a2[j:])
print(arr)
