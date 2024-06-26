n,m,p=map(int, input().split())
A=[]
for i in range(n):
    a=list(map(int,input().split()))
    A.append(a)
B=[]
for i in range(m):
    b=list(map(int,input().split()))
    B.append(b)

C= [[0] * p for _ in range(n)]
for i in range(n):
    for j in range(p):
        for k in range(m):
            C[i][j]+=A[i][k]*B[k][j]

for r in C:
    print(' '.join(map(str, r)))
