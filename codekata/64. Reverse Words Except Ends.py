userInput = input().split(" ")

res = ""

for i in userInput:
    if len(i)==1:
        res+=i+" "
    else:
        res += i[0:1]+i[1:-1][::-1]+i[-1:] + " "

print(res.strip())



