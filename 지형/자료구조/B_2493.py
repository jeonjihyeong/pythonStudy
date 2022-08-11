n = int(input())
tower = list(map(int,input().split()))
result = [0 for _ in range(n)]
stack=[]

for i in range(len(tower)-1,-1,-1):
    if len(stack)==0:
        stack.append([i,tower[i]])
    else:
        while tower[i]>stack[len(stack)-1][1]:
            towerlist = stack.pop()
            result[towerlist[0]]=i+1
            if len(stack)==0:
                break

        stack.append([i,tower[i]])

for num in result:
    print(num,end=" ")