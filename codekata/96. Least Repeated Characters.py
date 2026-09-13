N = input()

res = {}

out = ""

for i in N:
    if i in res:
        res[i]+=1
    else:
        res[i]=1

res.pop(" ",None)

newRes = dict(sorted(res.items(),key=lambda x:x[1]))

minCount = min(newRes.values())

for j in newRes.items():
    if j[1]==minCount:
        out += j[0]
    
print(out)

