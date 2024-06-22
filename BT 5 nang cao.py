n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

print('Pattern 1:')
for i in range(n):
    for j in range(n):
        print(mat[j][i], end=' ')
    print()
    
print('Pattern 2')
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(mat[i][j], end=' ')
    print()

print('Pattern 3')
for i in range(-1, -n-1, -1):
    for j in range(n):
        print(mat[j][i], end=' ')
    print()

print('Pattern 4')
for i in range(n):
    for j in range(-1, -n-1,-1):
        print(mat[i][j], end=' ')
    print()
