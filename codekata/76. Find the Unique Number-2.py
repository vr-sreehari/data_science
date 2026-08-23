N = input()
arr = input()

map1={}
for i in arr:
    map1[i]=arr.count(i)

for j in map1.items():
    if j[1]==1:
        print(j[0])
    

