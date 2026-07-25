userInput = input().split()
userInput1 = input()

count = 0

for i in userInput:
    if i==userInput1:
        count+=1

if(count>0):
    print(count)
else:
    print(-1)