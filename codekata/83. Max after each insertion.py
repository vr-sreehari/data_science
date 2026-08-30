N, K = map(int, input().split())

arr = list(map(int, input().split()))
insertions = list(map(int, input().split()))

current_max = max(arr)

result = []

for x in insertions:
    current_max = max(current_max, x)
    result.append(current_max)

print(*result)