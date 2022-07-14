import math

N = int(input())
number=list(map(int,input().split()))
count=0

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

for i in number:
    if i == 1: continue
    else:
        if primenumber(i)==True:
            count+=1
        elif primenumber(i)==False: continue


print(count)