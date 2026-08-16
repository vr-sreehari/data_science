N = input()
arr1 = list(map(int,input().split()))

sort1 = sorted(arr1)

res = sort1[len(sort1)-1]-sort1[0]

print(res)