N = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] < arr[j]:
            count += 1

if count > 0:
    print(count)
else:
    print(-1)

"""
N = int(input())
A = list(map(int, input().split()))

pairs = set()

for i in range(N):
    for j in range(i + 1, N):
        if A[i] < A[j]:
            pairs.add((A[i], A[j]))

print(len(pairs) if pairs else -1)
"""