N = int(input())
arr = list(map(int,input().split()))

res = []
var = 1

for a,i in enumerate(arr):
  if len(res):
      temp = res[len(res)-(a+1)] + i
  else:
    temp = arr[N-var]

  res.append(temp)
  var += 1
  
print(*res)

"""
N = int(input())
arr = list(map(int, input().split()))

res = []
total = 0

for value in arr:
    total += value
    res.append(total)

print(*res)
"""