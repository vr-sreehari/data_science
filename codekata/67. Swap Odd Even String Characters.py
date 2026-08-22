a = input()

b = []
c = []
res = ""

for i in a:
    if a.index(i)==0 or a.index(i)%2==0:
        b.append(i)
    else:
        c.append(i)

i = 0

while i < len(b):
    res += c[i]
    res += b[i]
    i+=1


print(res)


"""
a = input()

b = []
c = []
res = ""

for i, ch in enumerate(a):
    if i % 2 == 0:
        b.append(ch)
    else:
        c.append(ch)

i = 0

while i < len(c):
    res += c[i]
    res += b[i]
    i += 1

# If b has one extra character
if len(b) > len(c):
    res += b[-1]

print(res)
"""