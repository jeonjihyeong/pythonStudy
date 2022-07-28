import math

N= int(input())
nlist = list(map(int,input().split()))
M= int(input())
mlist = list(map(int,input().split()))
a= nlist[0]
b= mlist[0]

for i in range(1,N):
    a*=nlist[i]
for j in range(1,M):
    b*=mlist[j]
result=math.gcd(a,b)
if len(str(result))>9:
    result = str(result)
    print(result[-9:])
    
else: print(result)