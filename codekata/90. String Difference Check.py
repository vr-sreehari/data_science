s1,s2,K = input().split()

count=0

for i in s1:
    for j in s2:
        if i not in s2:
            count+=1
            break

if count==int(K):
    print("yes")
else:
    print("no")
