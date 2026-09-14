import math

N, R = map(int, input().split())

result = math.factorial(N) // math.factorial(N - R)

print(result)