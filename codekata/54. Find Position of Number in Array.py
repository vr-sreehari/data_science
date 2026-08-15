N,K = map(int,input().split())
arr = list(map(int,input().split()))

try:
    print(arr.index(K) + 1)
except ValueError:
    print(-1)