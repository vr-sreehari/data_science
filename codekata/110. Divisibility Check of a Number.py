N = int(input())

res = False
for i in range(2,N):
  if N%i==0:
    res = True

if res:
  print("yes")
else:
  print("no")