userInput = input()

value, target = userInput.split()

if(value.find(target)>=0):
    print(value.find(target) + 1)
else:
    print(-1)