N,K = input().split()
arr = list(map(int,input().split()))

res = set()

for i in arr:
    if arr.count(int(i))==int(K):
        res.add(i)

if len(res):
    print(" ".join(map(str,(res))))
else:
    print(-1)