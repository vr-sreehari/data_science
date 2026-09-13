N,K = input().split()

count=0

for i in N:
    if int(i)==int(K):
        count+=1

if count:
    print(count)
else:
    print(-1)

