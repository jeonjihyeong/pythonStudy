from itertools import permutations
n,m = map(int,input().split())

temp = []
for i in permutations(range(1,n+1),m):
    temp = list(i)
    print(' '.join(str(s) for s in temp))


