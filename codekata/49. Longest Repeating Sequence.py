N = int(input())
arr = list(map(int, input().split()))

current = 1
longest = 1

for i in range(1, N):
    if arr[i] == arr[i - 1]:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

if longest == 1:
    print(-1)
else:
    print(longest)