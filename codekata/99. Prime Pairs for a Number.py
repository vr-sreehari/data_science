n = int(input())

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


found = False

for i in range(2, int(n ** 0.5) + 1):

    if n % i == 0:
        j = n // i

        if is_prime(i) and is_prime(j):
            print(max(i, j), min(i, j))
            found = True
            break

if not found:
    print(-1)