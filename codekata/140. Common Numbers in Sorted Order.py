N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr1 = arr[:N]
arr2 = arr[N:N + M]

freq = {}
res = []

for i in arr1:
    freq[i] = freq.get(i, 0) + 1

for i in arr2:
    if i in freq and freq[i] > 0:
        res.append(i)
        freq[i] -= 1

res.sort()

print(*res)