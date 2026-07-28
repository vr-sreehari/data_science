N = int(input())
arr1 = input().split()
arr2 = input().split()

res = set(arr1) & set(arr2)

newRes = list(res)

if res:
    print(" ".join(sorted(newRes)))
else:
    print(-1)