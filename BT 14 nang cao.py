n=int(input())
mat=[[0]*n for i in range(n)]
x=1
u,d=0,n-1
l,r=0,n-1

while x<=n*n:
    for i in range(l,r+1):
        mat[u][i]=x
        x+=1
    u+=1
    
    for i in range(u,d+1):
        mat[i][r]=x
        x+=1
    r-=1
    
    for i in range(r,l-1,-1):
        mat[d][i]=x
        x+=1
    d-=1
    
    for i in range(d,u-1,-1):
        mat[i][l]=x
        x+=1
    l+=1
    
for r in mat:
    print(' '.join(map(str, r)))
