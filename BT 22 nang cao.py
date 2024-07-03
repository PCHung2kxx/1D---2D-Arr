n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

for i in range(len(mat)):
    if i%2!=0:
        mat[i].reverse()

for i in mat:
    print(' '.join(map(str,i)))
