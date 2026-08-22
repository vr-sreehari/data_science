N = input()
map1={}

for i,ch in enumerate(N):
    map1[ch]=N.count(ch)

count = 0

for j in map1.items():
    if(j[1]>count):
        count = j[1]
    
print(count)

