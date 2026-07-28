N,X = input().split()
arr = list(map(int,input().split()))

seen = set()

for i in arr:
    if int(X)-i in seen:
        print("yes")
        break
    seen.add(i)
else:
    print("no")

            
