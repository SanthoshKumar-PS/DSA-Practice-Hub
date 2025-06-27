def spiralOrder( matrix):
    if not matrix or not matrix[0]:
        return []

    m=len(matrix)
    n=len(matrix[0])
    top,bottom,left,right=0,m-1,0,n-1
    arr=[]

    while left<=right and top<=bottom:
        for i in range(left,right+1):
            arr.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            arr.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                arr.append(matrix[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                arr.append(matrix[i][left])
            left+=1
    return arr


print([1, 2, 3, 6, 9, 8, 7, 4, 5])
matrix= [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix));