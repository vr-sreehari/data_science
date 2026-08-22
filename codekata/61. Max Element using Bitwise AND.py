userInput = input()
userInput2 = list(map(int,input().split()))

large = 0

for i in userInput2:
    if i>large:
        large=i

print(large)