def fibo(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        return fibo(n-2)+fibo(n-1)

n=int(input())
mat=[[0]*n for i in range(n)]
u,d=0,n-1
l,r=0,n-1
dem=0


while dem<n*n:
    for i in range(l,r+1):
        if dem >= n*n: break
        mat[u][i]= fibo(dem)
        dem+=1
    u+=1
    
    for i in range(u,d+1):
        if dem >= n*n: break
        mat[i][r]=fibo(dem)
        dem+=1
    r-=1

    for i in range(r,l-1,-1):
        if dem >= n*n: break
        mat[d][i]=fibo(dem)
        dem+=1
    d-=1
    
    for i in range(d,u-1,-1):
        if dem >= n*n: break
        mat[i][l]=fibo(dem)
        dem+=1
    l+=1
    
for r in mat:
    print(' '.join(map(str, r)))
