N = input()
arr = list(map(int,input().split()))

even = []
odd = []

for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

if len(even)==1:
    print("".join(map(str,even)))
elif len(odd)==1:
    print("".join(map(str,odd)))
else:
    print(-1)