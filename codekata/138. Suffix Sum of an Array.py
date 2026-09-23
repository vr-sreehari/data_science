N = int(input())
arr = list(map(int,input().split()))

res = []
var = 1
total = sum(arr)

for a,i in enumerate(arr):
  if len(res):
      temp = res[len(res)-1] - arr[a-1]
  else:
    temp = total

  res.append(temp)
  var += 1
  
print(*res)