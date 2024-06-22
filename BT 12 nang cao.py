n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)
    
def chuyenvi(mat):
    cot=len(mat[0])
    hang=len(mat)
    newmat=[]
    for i in range(cot):
        l=[]
        for j in range(hang):
            l.append(mat[j][i])
        newmat.append(l)
    return newmat

mat2=chuyenvi(mat)
for i in mat2:
    i.sort()
mat3=chuyenvi(mat2)
for j in mat3:
    print(' '.join(map(str, j)))
