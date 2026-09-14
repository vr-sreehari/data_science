import math

P, A = map(int, input().split())

if P % 2 != 0:
    print("no")
else:
    s = P // 2

    d = s * s - 4 * A

    if d < 0:
        print("no")
    else:
        root = math.isqrt(d)

        if root * root == d and (s + root) % 2 == 0:
            print("yes")
        else:
            print("no")