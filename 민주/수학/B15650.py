


n, m = map(int, input().split())

answer = []
temp = []

def dfs(idx, list):
    if len(list) == m:
        answer.append(list)

        return

    for i in range(idx, n):  
   
        dfs(i+1,list+[i+1])



dfs(0, [])
for i in answer:
    print(" ".join(str(s) for s in i))

