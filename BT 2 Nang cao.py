m,n=map(int,input().split())
mat=[]
for i in range(m):
    r=list(map(int, input().split()))
    mat.append(r)

def calc(mat):
    for i in range(len(mat)):
        print(sum(mat[i]), end=' ')
    print()

def chuyenvi(mat):
    cot=len(mat[0])
    hang=len(mat)
    newmat=[]
    for i in range(cot):
        l=[]
        for j in range(hang):
            l.append(mat[j][i])
        newmat.append(l)
    return newmat

calc(mat)
calc(chuyenvi(mat))
