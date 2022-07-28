import math

def Gcd(a,b):
    if a < b:
        a, b = b, a
    while a > 0:
        b, a = a, b%a
    return b

n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

new = [] # arr[i+1] - arr[i] 값 저장
result = [] # 최대공약수의 약수 값 저장

for i in range(len(arr)-1):
    new.append(arr[i+1]-arr[i])

gcd = new[0]

for i in range(1,len(new)):
    gcd = Gcd(new[i],gcd)

for i in range(2,int(math.sqrt(gcd))+1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd//i)
        
result.append(gcd) #2부터 확인하여 1과 대응되는 자기 자신 추가
result = sorted(list(set(result))) # 중복 제거 ex) 4의 약수 1,2,4 면 2가 중복해서 들어간다.
print(" ".join(map(str,result))) # print(*result)
