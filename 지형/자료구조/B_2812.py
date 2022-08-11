N,K = map(int, input().split())
N_number =list(map(int,input().strip()))

K_number=K
result = []

for i in range(N):
    while K_number>0 and result:
        if result[len(result)-1]<N_number[i]:
            result.pop()
            K_number-=1
        else:
            break
    result.append(N_number[i])

for i in range(N-K):
    print(result[i],end="")