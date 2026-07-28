userInput = int(input())

arr = list()
res = list()

for i in range(userInput):
    if userInput%(i+1) == 0:
        arr.append(i+1)

for j in arr:
    if (userInput/j)%2!=0:
        res.append(j)
    
print(res[0])