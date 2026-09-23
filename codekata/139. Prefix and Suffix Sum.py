N = int(input())
arr = list(map(int,input().split()))

suffix = []
prefix = []
var = 1
total = sum(arr)
res = []

for value in arr:
    total += value
    prefix.append(total)
  
for a,i in enumerate(arr):
  if len(suffix):
      temp = suffix[len(suffix)-1] - arr[a-1]
  else:
    temp = 0

  suffix.append(temp)
  var += 1

for i in range(N):
  res.append(suffix[i]+prefix[i])

print(*res)