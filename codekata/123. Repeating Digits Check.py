N = (input())

res = {}
out = False

for i in N:
  res[i] = N.count(i)

for j in res.values():
  if j>1:
    out = True
    break

if out:
  print("yes")
else:
  print("no")