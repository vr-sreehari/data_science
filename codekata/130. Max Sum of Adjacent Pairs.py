N = int(input())
arr= input().split()

count = 0

for i in range(N-1):
  count += max(int(arr[i]),int(arr[i+1]))

print(count)



