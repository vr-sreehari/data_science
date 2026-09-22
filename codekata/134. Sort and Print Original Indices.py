import sys

data = list(map(int, sys.stdin.read().split()))

N = data[0]
arr = data[1:N + 1]

pairs = []

for i in range(N):
    pairs.append((arr[i], i + 1))

pairs.sort()

result = []

for value, index in pairs:
    result.append(index)

print(*result)