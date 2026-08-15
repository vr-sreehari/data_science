S1,S2 = input().split()

#res = list(S1) ^ list(S2)

res = []

for i in list(S1):
    if i not in list(S2):
        res.append(i)
        
if res:
    print("".join(res))
else:
    print(-1)