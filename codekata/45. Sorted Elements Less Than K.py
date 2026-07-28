N, K = map(int, input().split())
arr = list(map(int, input().split()))

sort = sorted(arr)

res = []

for i in sort:
    if K>i:
        res.append(str(i))

if(len(res)):
    print(" ".join(res).strip())
else:
    print(-1)