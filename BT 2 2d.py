from random import *
a=[]
n=int(input())
for i in range(n):
    b=[]
    for j in range(n):
        b.append(randint(1,10))
    a.append(b)
    
print(a)
