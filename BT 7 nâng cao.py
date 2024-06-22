n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)
u,v=map(int,input().split())

mat[u-1], mat[v-1]=mat[v-1], mat[u-1]
for j in mat:
    print(' '.join(map(str, j)))
