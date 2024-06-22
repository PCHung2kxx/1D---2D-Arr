n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

for i in mat:
    i.sort()

for j in mat:
    print(' '.join(map(str, j)))
