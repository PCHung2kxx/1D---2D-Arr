n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

def tamgiac(mat):
    mat2=[]
    for i in range(len(mat)):
        mat2.append(mat[i][:i+1])
    return mat2

dem=0
mat2=tamgiac(mat)
for i in mat2:
    for j in i:
        if str(j)==str(j)[::-1]:
            dem+=1
print (dem)
