n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

for i in range(1,len(mat)-1):
    for j in range(1,len(mat[i])-1):
        if j!=0 or j!=len(mat[i])-1:
            mat[i][j]=' '

for r in mat:
    for c in r:
        print(c, end=' ')
    print()
