N = int(input())
arr = list(map(int, input().split()))

result = 0

for i in range(N - 1):
    result += arr[i] + arr[i + 1]

print(result)