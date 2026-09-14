N = int(input())
arr = list(map(int, input().split()))

result = arr[0]

for i in range(1, N):
    result ^= arr[i]

print(result)