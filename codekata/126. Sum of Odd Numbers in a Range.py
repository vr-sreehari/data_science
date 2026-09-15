L,R = list(map(int,input().split()))

count = 0

for i in range(L,R+1):
  if i%2!=0:
    count+=i

print(count)


