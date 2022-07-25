S= int(input())
a= 0

for i in range(1,S+1):
    if S==1:
        print(1)
        break
    a= a+i
    if a>S:
        print(i-1)
        break