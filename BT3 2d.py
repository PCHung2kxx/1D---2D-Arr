m,n=map(int,input().split())

l=[]
for i in range(m):
    l2=[]
    for j in range(n):
        k=int(input())
        l2.append(k)
    l.append(l2)

def chuyenvi(mat):
    cot=len(mat[0])
    hang=len(mat)
    newmat=[]
    for i in range(cot):
        l=[]
        for j in range(hang):
            l.append(mat[j][i]) #đổi hàng thành cột
        newmat.append(l)
    return newmat

print(chuyenvi(l))
