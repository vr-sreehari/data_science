userInput1,userInput2 = input().split()

result = False

for i in userInput1:
    if i in userInput2:
        result=True
        break

if(result):
    print("yes")
else:
    print("no")
            
