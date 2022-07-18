import math
a = int(input())
answer=[]

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

for i in range(2,10000):
    if primenumber(i)==True:
        answer.append(i)
    else: continue

for _ in range(a):
    b= int(input())
    c= b//2
    for j in range(c,1,-1):
        if primenumber(j)== True and primenumber(b-j):
            print(j, b-j)
            break
    