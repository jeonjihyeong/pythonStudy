from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    command = input().split()
    length = len(queue)
    
    if command[0] == "push_front":
        queue.appendleft(command[1])
    
    if command[0] == "push_back":
        queue.append(command[1])
        
    if command[0] == "pop_front":
        if length == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    if command[0] == "pop_back":
        if length == 0:
            print(-1)
        else:
            print(queue.pop())
            
    if command[0] == "size":
        print(length)
        
    if command[0] == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
            
    if command[0] == "front":
        if length == 0:
            print(-1)
        else:
            print(queue[0])
            
    if command[0] == "back":
        if length == 0:
            print(-1)
        else:
            print(queue[-1])