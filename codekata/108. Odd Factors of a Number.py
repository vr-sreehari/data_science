N = int(input())

arr = []

for i in range(1,N+1):
  if N%i==0:
    if i%2!=0:
      arr.append(str(i))

print(" ".join(arr))