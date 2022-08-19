n, k = map(int,input().split())
arr = [i for i in range(1,n+1)]

idx = 0
print("<")

while len(arr)!=0:
    print(arr)
    print("idx",idx)
    
    if k > len(arr):
        idx = k % len(arr) + idx
        print("idx2",idx)
        if idx > len(arr):
            idx = len(arr) - idx
            print("idx3",idx)
        print(arr[idx-1])
        arr.remove(arr[idx-1])
        idx-=1  
        continue
        
    idx+=k
    if idx > len(arr):
        idx = idx - len(arr)
    
            
    print(arr[idx-1])
    arr.remove(arr[idx-1])
    idx-=1
print(">")