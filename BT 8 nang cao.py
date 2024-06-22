n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)
u,v=map(int,input().split())

for i in mat:
    i[u-1], i[v-1]=i[v-1], i[u-1]

for j in mat:
    print(' '.join(map(str, j)))
