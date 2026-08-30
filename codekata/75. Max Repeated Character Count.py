N = input()
map1={}

for i,ch in enumerate(N):
    map1[ch]=N.count(ch)

count = 0

for j in map1.items():
    if(j[1]>count):
        count = j[1]
    
print(count)

"""
s = input()

frequency = {}

for char in s:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

maximum = 0

for value in frequency.values():
    if value > maximum:
        maximum = value

if maximum > 1:
    print(maximum)
else:
    print(0)
"""
