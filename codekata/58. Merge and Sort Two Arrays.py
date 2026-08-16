N,M = input().split()
arr1 = list(map(str,input().split()))
arr2 = list(map(str,input().split()))

sort1 = sorted(arr1)
sort2 = sorted(arr2)

res = list(filter(None,sorted(" ".join(sort1) + " " + " ".join(sort2))))

print(" ".join(res).strip())