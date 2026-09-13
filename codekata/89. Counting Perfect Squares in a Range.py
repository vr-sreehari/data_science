import math

L, R = map(int, input().split())

count = 0

for n in range(L, R + 1):
    root = math.isqrt(n)

    if root * root == n:
        count += 1

if count == 0:
    print(-1)
else:
    print(count)