userInput = input()

unique = set()
unique2 = set()

for i in userInput:
    if i in unique:
        unique2.add(i)
    unique.add(i)
    
for j in unique2:
    unique.remove(j)

if len(unique):
    print(len(unique))
else:
    print(-1)


