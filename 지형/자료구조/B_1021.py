from collections import deque

from collections import deque

n,m = map(int,input().split())
queue = deque([i for i in range(1,n+1)])
number = list(map(int,input().split()))

count = 0
for i in number:
    while 1:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue)//2:
                queue.rotate(-1)
                count += 1
            else:
                queue.rotate(1)
                count += 1

print(count)