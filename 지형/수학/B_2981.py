import math

N=int(input())
n=[]
result =[]
for i in range(N):
    n.append(int(input()))
n=sorted(n)
a=[]
for i in range(N-1):
    temp = n[i+1]-n[i]
    a.append(temp)
gcd=int(max(a))

for j in a:
    gcd=math.gcd(gcd,j)
for i in range(2,int(gcd**0.5)+1):
    if gcd%i==0:
        result.append(i)
        result.append(gcd//i)
result.append(gcd)
result=list(set(result))
result.sort()
for i in result:
    print(i, end=" ")