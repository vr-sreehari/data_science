n, k = map(int, input().split())

res = 0

for i in range(1, min(n, k) + 1):
    if n % i == 0 and k % i == 0:
        res = i

print(res)