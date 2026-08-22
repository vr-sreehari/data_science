N,K = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(K):
    x = arr.pop()
    arr.insert(0,x)
    
print(*arr)

"""
N, K = map(int, input().split())
a = list(map(int, input().split()))

K = K % N

a = a[-K:] + a[:-K]

print(*a)
"""