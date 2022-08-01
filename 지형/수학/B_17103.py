import math

n= int(input())
a=[]
prime_number=[]
for i in range(n):
    a.append(int(input()))

max_a=max(a)
check = [True for _ in range(max_a)]

for i in range(2,int(max_a**0.6)):
    if check[i]==True:
        for j in range(i*2, max_a, i) : 
            if check[j] == True :
                check[j] = False    


for i in a:
    cnt= 0
    for j in range(2,i//2+1):
        if check[j]==True and check[i-j]==True:
            cnt+=1
    print(cnt)