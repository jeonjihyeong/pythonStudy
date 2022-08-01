import math

N,S= map(int, input().split())
A= list(map(int, input().split()))
D_list = []
for i in A:
    c=abs(S-i)
    D_list.append(c)
D=D_list[0]
for i in D_list:
    D=math.gcd(i,D)

print(D)