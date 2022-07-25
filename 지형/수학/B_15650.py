N,M=map(int,input().split())
s=[]

def dfs(n,s):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n,N+1):
        if i not in s:
            s.append(i)
            n+=1
            
            dfs(n,s)
            s.pop()

n=1       
dfs(n,s)