a,b = input().split()

map1={}
count=0

if len(a)!=len(b):
    res="no"
    
for i in range(len(a)):
    x=a[i]
    y=b[i]
    map1[x]=y

for j in map1.items():
    if(not j[0]==j[1]):
        count+=1

if count==1:
    print("yes")
else:
    print("no")


"""
a, b = input().split()

if len(a) != len(b):
    print("no")
else:
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    if count == 1:
        print("yes")
    else:
        print("no")
"""



