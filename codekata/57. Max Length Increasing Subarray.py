N = input()
arr = list(map(int,input().split()))

val = 1
res = 1

for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        val+=1
        if val>res:
            res=val
    else:
        val = 1

if res>1:
    print(res)
else:
    print(-1)
    