N = int(input())

arr = input().split()

arr.sort(key=lambda x: (len(x), x))

print(*arr)