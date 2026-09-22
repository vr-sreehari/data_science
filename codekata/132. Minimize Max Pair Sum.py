N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

pairs = N - 1
result = 0
i = 0

while pairs >= 2:
    result += 2 * arr[i]
    i += 1
    pairs -= 2

if pairs == 1:
    result += arr[i]

print(result)

"""
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = sum(arr[1:])

print(result)
"""