N = list(input())
answer = 0
stack = []

for i in range(len(N)):
    if N[i] == '(':
        stack.append('(')

    else:
        if N[i-1] == '(': 
            stack.pop()
            answer += len(stack)

        else:
            stack.pop() 
            answer += 1 

print(answer)