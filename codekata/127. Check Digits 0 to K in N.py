N,K = list(map(str,input().split()))

res = True

for i in range(int(K)):
  if(N.find(str(i)))==-1:
    res=False

if res:
  print("yes")
else:
  print("no")


