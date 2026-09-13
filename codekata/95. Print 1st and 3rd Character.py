N = input()

res = ""

for i,ch in enumerate(N,start=1):
    if (i==1 or i==3):
        res+=ch

print(res)

