n=int(input())
mat=[]
for i in range(n):
    r=list(map(int,input().split()))
    mat.append(r)

l=[]
dem=0

for i in range(n):
    if i==n-1-i:
        l.append(mat[i][i])
    else:
        l.append(mat[i][i])
        l.append(mat[i][n-1-i])

def snt(a):
    if a<=3:
        return a>1
    if a%2==0 or a%3==0:
        return False
    i=5
    while i<=a**0.5:
        if a%i==0 or a%(i+2)==0:
            return False
        i+=6
    return True

for i in l:
    if snt(i):
        dem+=1

print(dem)
