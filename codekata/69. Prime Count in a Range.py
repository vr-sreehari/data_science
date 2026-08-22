a,b = map(int,input().split())

res = 0

for n in range(a,b+1):
    if n < 2:
        continue

    prime = True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        res+=1

print(res)




