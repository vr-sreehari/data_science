M = input()
arr = list(map(int,input().split()))

sort = sorted(arr)

index = arr.index(sort[0])

if index:
    print(index)
else:
    print(-1)