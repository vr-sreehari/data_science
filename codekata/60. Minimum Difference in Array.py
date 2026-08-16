N = input()
arr1 = list(map(int,input().split()))

sort1 = sorted(arr1)

val = 0
res = []

for i in range(len(sort1)-1):
        val = sort1[i+1]-sort1[i]
        res.append(val)
        
print(sorted(res)[0])
