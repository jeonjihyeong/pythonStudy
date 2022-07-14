M,N = map(int, input().split())

number = [True] * (N+1)

x=int((N+1)**0.5)

for i in range(2,x+1):
    if number[i]==True:
        j=2
        while i*j<=N:
            number[i*j]= False
            j+=1
            

for i in range(M,N+1):
    if i ==1:
        continue
    else:
        if number[i]==True:
            print(i)
        else: continue