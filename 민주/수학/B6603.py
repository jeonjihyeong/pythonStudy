# from itertools import combinations
# while True:
#     arr = list(map(int,input().split()))
#     if arr[0] == 0:
#         break
#     for i in combinations(arr[1:],6):
#         print(' '.join(map(str,list(i))))
#     print()

def combination(idx, temp):
    if len(temp) == 6:
        answer.append(temp[:])
        return
    for i in range(idx, arr[0]):
        combination(i+1,temp+[arr[i+1]])
    


while True:
    answer = []
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    combination(0,[])
    print(answer)
    for i in answer:
        print(" ".join(map(str,i)))
    print()
    
    