N = input()
arr = input()

map1={}
for i in arr:
    map1[i]=arr.count(i)

for j in map1.items():
    if j[1]==1:
        print(j[0])
    

"""
n = int(input())

arr = list(map(int, input().split()))

count = {}

for num in arr:

    if num in count:
        count[num] = count[num] + 1

    else:
        count[num] = 1


for num in arr:

    if count[num] == 1:
        print(num)
        break
"""
