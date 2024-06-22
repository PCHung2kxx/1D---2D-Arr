m,n=map(int,input().split())
l=[]
for i in range(m):
    r=list(map(int, input().split()))
    l.append(r)

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
    a=[]
    for j in i:
        if snt(j):
            a.append(str(j))
    print(' '.join(a))
