N = int(input())

for i in range(N):
    stack = []
    M = input()
    for j in M:
        if j=='(':
            stack.append(j)
        elif sj==')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else: print("YES")