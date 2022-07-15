from itertools import permutations
n,m = map(int,input().split())
arr = list(range(1,n+1))
k=list(permutations(arr,m))
for i in k:
    print(' '.join(map(str,i)))