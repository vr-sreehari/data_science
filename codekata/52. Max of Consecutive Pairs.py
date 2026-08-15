N = input()
arr = list(map(int,input().split()))

res = []

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        res.append(arr[i])
    else:
        res.append(arr[i+1])

print(" ".join(map(str,res)))