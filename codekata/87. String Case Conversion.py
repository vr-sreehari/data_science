userInput = input()

res = []
for i in userInput:
    if i.isupper():
       res.append(i.lower()) 
    else:
        res.append(i.upper())
        
print("".join(res))