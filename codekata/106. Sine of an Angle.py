import math

A = float(input())

result = round(math.sin(math.radians(A)), 10)

if result.is_integer():
    print(int(result))
else:
    print(result)