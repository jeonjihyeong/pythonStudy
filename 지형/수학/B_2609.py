a, b= map(int, input().split())
small_number=min(a,b)
for i in range(small_number,0,-1):
    if b%i==0:
        if a%i==0:
            print(i)
            break
x=1
y=1
while True:
    result_a=a*x
    result_b=b*y
    if result_a<result_b:
        x+=1
    elif result_a>result_b:
        y+=1
    elif result_a==result_b:
        print(result_a)
        break
