n = int(input())
number = list(map(int,input().split()))
result = [-1]*n
stack=[]

stack.append(0)
for i in range(1,n):
    while stack and number[stack[-1]]<number[i]:
        result[stack.pop()]=number[i]
    stack.append(i)

print(*result)