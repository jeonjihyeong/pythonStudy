N_amount=int(input())
N_list=list(map(int,input().split()))
N=sorted(N_list)
result=N[0]*N[-1]
print(result)