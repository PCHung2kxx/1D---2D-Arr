n,m=map(int,input().split())
l=[]
for i in range(m):
    r=list(map(int, input().split()))
    l.append(r)

def findminmax(mat):
    minval=float('inf')
    maxval=0
    minpos=[]
    maxpos=[]
    for n in range(len(mat)):
        for m in range(len(mat[0])):
            val=mat[n][m]
            if val<minval:
                minval=val
                minpos=[[n+1,m+1]]
            elif val==minval:
                minpos.append([n+1,m+1])
            
            if val>maxval:
                maxval=val
                maxpos=[[n+1,m+1]]
            elif val==maxval:
                maxpos.append([n+1,m+1])
    return minval,maxval,minpos,maxpos

minval,maxval,minpos,maxpos=findminmax(l)

print(minval)
for i in minpos:
    print(i[0],i[1])

print(maxval)
for j in maxpos:
    print(j[0],j[1])
