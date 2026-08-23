def is_prime(a):
    if a < 2:
        return False
    else:
        prime = True
        for i in range(2, a):
            if a % i == 0:
                prime = False
                break
    if prime:
        return True
    else:
        return False
    
N = int(input())

res = ""

for i in range(2,N+1):
    if N % i == 0 and is_prime(i):
        res += str(i) + " "
        
print(res.strip())

