import math
answer=[]

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True

for i in range(2,246913):
    if primenumber(i)==True:
        answer.append(i)
    else: continue
while True:
    a = int(input())
    result =0
    if a== 0:
        break
    for i in answer:
        if a<i<=2*a:
            result+=1
    print(result)