N = int(input())
arr = list(map(int,input().split()))

print(*set(arr))

"""
N = int(input())
arr = list(map(int, input().split()))

result = list(dict.fromkeys(arr))

print(*result)
"""