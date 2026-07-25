userInput = input()

value, target = userInput.split()

count = 0

for i in value:
    if(i==target):
        count+=1

if(count>0):
    print(count)
else:
    print(-1)