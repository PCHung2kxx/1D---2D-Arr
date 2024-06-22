n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

for i in range(n):
    mat[i][i], mat[i][n-1-i]=mat[i][n-1-i], mat[i][i] 

for i in mat:
    print(' '.join(map(str, i)))
