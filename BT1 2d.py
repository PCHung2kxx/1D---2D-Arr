def sinhmatrix (m,n):
    mat=[[0 for i in range(n)] for j in range(m)]
    for q in range(m):
        if n-q-1<n:
            mat[q][n-q-1]=1
    return mat

m,n=map(int,input().split())
print(sinhmatrix(m,n))
