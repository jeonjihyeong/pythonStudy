N = int(input())
a = input()
a_list=[]

for i in range(N):
    a_list.append(int(input()))

stack = []
for i in a:
    if 'A' <= i <= 'Z':
        stack.append(a_list[ord(i)-65])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i =='+':
            stack.append(str1+str2)
        elif i =='-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print('%.2f' %stack[0])